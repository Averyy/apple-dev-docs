# Leveraging the declarative management data model to scale devices

**Framework**: Device Management

Use declarative management to make devices more autonomous and proactive.

#### Overview

Declarative Device Management, introduced in iOS 15, uses a declarative data model paradigm. This paradigm allows servers to avoid the common performance and scalability issues typically associated with serializing commands and polling devices over MDM.

While declarative management is a new paradigm, it’s not a new protocol: the protocol has been added to the existing MDM protocol to make adoption simpler.

The declarative management data model has three key components: declarations, that support device functionality, status, used to track changes in device state, and extensibility, allowing devices and servers to advertise the changes in their capabilities over time.

##### Use Declarations to Define Policies Specify Assets and Store Organizational Information

Declarations are payloads the server defines and synchronizes to the device with the declarative management protocol. They represent policies the organization wants to enforce on the device, and other items such as management metadata.

Declarations are a schema-driven data model, serialized as JSON objects. Each declaration has a common set of keys, each one of them required.

| Key | Type | Content |
| --- | --- | --- |
| `Type` | String | The declaration type. A dot-separated sequence of tokens. |
| `Identifier` | String | The unique identifier within the set of all declarations sent to a device. This is typically a UUID string. |
| `ServerToken` | String | An identifier for a unique revision of the declaration. |
| `Payload` | Dictionary | A data-specific piece of the declaration, containing the keys and values for the declaration type. |

The `Type` defines the type of the declaration. Standard types have a `com.apple.` prefix. The next component of the type is either `activation`, `asset`, `configuration`, or `management`. Each declaration type has its own additional components that group together similar items. For example, configurations representing different types of accounts have a `com.apple.configuration.account.` prefix.

The `Identifier` uniquely identifies a single declaration within the set of all declarations sent to a device. This is typically a UUID value. When synchronizing declarations between server and device, this value is the primary key used to match the set of declarations sent by the server with the set the device previously received.

The `ServerToken` key represents a revision of a specific declaration. For example, a declaration with `Identifier` set to `A` and `ServerToken` set to `2`, is an update to a declaration with `Identifier` set to `A` and `ServerToken` set to `1`. The value of this key could be a UUID or a simple counter. When any part of the declaration Payload changes, update this value for correct synchronization to occur.

The combination of `Identifier` and `ServerToken` allows the device to determine which declarations are new, changed, or removed, during a synchronization operation.

The `Payload` key is an object representing the data pertinent to the declaration type. A formal schema defines the necessary and optional data for each declaration type. Values can be strings, numbers, booleans, arrays, or dictionaries, and may be constrained in range, such as numbers 1 through 10, or to a specific set of values like a string enumeration.

Every declaration has an associated `active` and `valid` state that the device shares with the server through the status channel. There are four types of declarations, Configurations, Assets, Activations, and Management.

###### Use Configuration Declarations to Define the Policies

Configurations represent the policy applied to a device. For example, accounts, settings and restrictions, network setup, fonts, and so on. Configurations are similar to MDM’s profile payloads.

A configuration has an `active` state which is `true` if the device is implementing the policy defined by the configuration, and `false` otherwise.

A configuration has a `valid` state which can have 3 values:

- `valid`: The system has checked the configuration and it’s valid.
- `invalid`: The system has checked the configuration and it’s not valid.
- `unknown`: The system hasn’t checked the configuration.

A configuration is valid if it meets the following conditions:

- The configuration was successfully synchronized from the server.
- The configuration is a valid JSON object conforming to the schema defined by the configuration type.
- All referenced assets are valid.
- The device can apply the policy when the configuration is active.

###### Use Asset Declarations to Specify Additional Data

Assets represent ancillary data needed by configurations. There are two main use cases for assets:

- Large data: a large item of data, such as an image, a font, or entire font suite. In this case, the asset’s Payload contains a key with a URL value pointing to the actual data. This allows shifting the distribution of large data items from the management server to a server more suited to handling such traffic (for example, a content delivery network). The data for the asset is only downloaded when needed.
- Personal data: user specific data such as a name, email address, passwords for accounts, or certificates. This takes the per-user customized data out of configurations, and moves it into smaller, dedicated objects.

Assets have a one-to-many relationship with configurations: one asset may be referenced by many configurations. The reference takes the form of a specific key in a configuration payload whose value is the `Identifier` key value of the asset.

The data for an asset can be independently updated, without needing to update the configuration that references it. The system can make small, incremental updates to per-user data, or large data items, shared across many configurations.

An asset has an `active` state which is `true` if at least one active configuration references the asset, and `false` otherwise.

An asset has a `valid` state which can have 3 values:

- `valid`: The system has checked the asset and it’s valid.
- `invalid`: The system has checked the asset and it’s not valid.
- `unknown`: The system hasn’t checked the asset.

An asset is valid if it meets the following conditions:

- The asset was successfully synchronized from the server.
- The asset is a valid JSON object conforming to the schema defined by the asset type.
- All referenced asset data is successfully downloaded when the asset is active.

###### Use Activation Declarations to Apply Logic to Your Configurations

Activations specify the logic that determines how and when, the system applies the policies defined by configurations to the device. Activations contain a set of configurations that the system applies atomically to the device, such that the system applies all referenced configurations together, or none. Therefore all of the configurations, and assets referenced by those configurations, must be valid in order for the system to apply the activation.

An activation has an `active` state which is `true` if the activation will attempt to apply the policies defined by its configurations, and `false` otherwise.

An activation has a `valid` state which can have 3 values:

- `valid`: The system has checked the activation and it’s valid.
- `invalid`: The system has checked the activation and it’s not valid.
- `unknown`: The system hasn’t checked the activation.

An activation is valid if it meets the following conditions:

- The activation was successfully synchronized from the server.
- The activation is a valid JSON object conforming to the schema defined by the activation type.

Activations have a many-to-many relationship with configurations: one activation can reference many configurations, and many activations can reference the same configuration.

If at least one activation that references a configuration is active, the system applies the policies defined by the configuration.

An activation can include a predicate defining an expression that the system evaluates, and the result used to determine whether the activation should be active or inactive, subject to other rules governing activations (as described above).

A predicate is a string conforming to Apple’s [`Predicate Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789). A string value that doesn’t conform to the predicate syntax is an error, and the activation isn’t activated.

The predicate expression can include references to declarative device management data such as status items and management properties, that conform to Apple’s Key-Value protocol (see [`About Key-Value Coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107) for more information). Referenced items must appear in the predicate inside of an extension term to correctly delineate them from other predicate terms and allow use of characters not typically allowed in predicate tokens.

This is an example of a predicate that checks whether the device is an iPad:

```other
(@status(device.model.family) == 'iPad')
```

###### Use Management Declarations to Define Organizational Data

Management declarations convey management metadata such as information about the organization managing the device, as well as details about the server’s supported features.

A management declaration has an `active` state which is always `false` and not part of the activation process.

A management declaration has a `valid` state which can have 3 values:

- `valid`: The system has checked the management declaration and it’s valid.
- `invalid`: The system has checked the management declaration and it’s not valid.
- `unknown`: The system hasn’t checked the management declaration.

A management declaration is valid if it meets the following conditions:

- The management declaration was successfully synchronized from the server.
- The management declaration is a valid JSON object conforming to the schema defined by the management declaration type.

##### Use Status to Report Device State

Devices report changes in device state back to the server as JSON status items, using a status report. There are several categories of device states:

- Management states - the valid and active states for all declarations on the device, and any error details describing why a declaration is invalid or inactive.
- Device properties - properties of the device (for example, device model, OS version, etc).
- Other properties (accounts, passcode, and MDM installed apps).

A status item contains a status name (similar to a “key path”) and an associated value. A status name is a string containing a dot-separated sequence of tokens (for example, device.identifier.serial-number). Each segment of the name defines a key in the overall hierarchical status dictionary.

Consider the following three status items: `device.identifier.serial-number`, `device.identifier.udid`, and `management.push-token`. The status reported by the device would be:

```other
{
   "device": {
      "identifier": {
         "serial-number": "abc123",
         "udid": "d4bffb90be0845c6a8b8184a7e06d487"
      }
   },
   "management": {
      "push-token": "xyz789"
   }
}
```

A status item’s value can be a string, number, boolean, null, or array.

Status item arrays have values containing JSON objects with a well-defined schema, with the same schema used for all items in an array. The schemas are specific to the type of item the status represents. Devices report changes to array status items incrementally (see [`StatusReport`](statusreport.md) for additional details).

To receive updates for status items as they change, the server must subscribe to each status item by sending a [`ManagementStatusSubscriptions`](managementstatussubscriptions.md) declaration to the device. All management status items (those that begin with the `management.` name prefix) are automatically reported to the server, and don’t need to be referenced in a status subscription.

When the status of a device changes or a status subscription declaration becomes active, the device sends a [`StatusReport`](statusreport.md) to the server.

##### Use Client and Server Capabilities to Match Feature Sets

The set of capabilities and features supported by declarative management can vary over time as the system adds, modifies and deprecates items. Devices and servers advertise their capabilities and features to each other, so they can adopt new behaviors even as the server and device are independently upgraded, without the need to keep them in lock-step.

The device advertises the set of declaration types and status items it supports with the [`StatusManagementClientCapabilities`](statusmanagementclientcapabilities.md) status item. When the device enables declarative management, the device sends this status item to the server. Servers need to persist this on a per-enrollment basis as the set of capabilities might vary by more than just device type or operating system version. The server shouldn’t send declarations to the device that it hasn’t advertised as supported.

The server advertises the set of protocol features it supports through the [`ManagementServerCapabilities`](managementservercapabilities.md) declaration that it sends to the device when it enables declarative management. If the server capabilities change any time after enablement, then the server should use the normal declaration synchronization process to update the device with the new values.

## See Also

- [Integrating Declarative Management](integrating-declarative-management.md)
  Use the declarative management protocol to manage MDM features such as device enrollment and un-enrollment and device and user authentication.
- [Deploying apps with declarative management](deploying-apps-with-declarative-management.md)
  Use declarative app configurations to deploy managed apps to devices.
- [Declarations](devicemanagement-declarations.md)
  The available declarations for device management.
- [Status Reports](status-reports.md)
  Reports from the device about its current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/leveraging-the-declarative-management-data-model-to-scale-devices)*