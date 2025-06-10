# Specifying and decoding a configuration

**Framework**: ManagedApp

Publish a configuration specification and implement a decoder that parses and validates configuration provided by an MDM admin.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

#### Overview

Your app can allow device management administrators (MDM admins) to configure properties that customize your app’s user experience on a specific device or a collection of devices. To provide this functionality, implement a configuration class. To be effective, ensure that your configuration class:

- Contains the information for features that fulfill an organization’s needs
- Decodes and validates the configuration that MDM admins supply
- Generates actionable errors so MDM admins can troubleshoot in the event that they provide an invalid configuration

You define the configurable options that your app offers. For example, your app can specify that the following data is configurable: a server URL that has a customizable region, a timeout, and a role property that selectively enables user interface based on a person’s job function. The following image illustrates such a configuration:

![An entity-relationship diagram that contains a box titled Configuration. Inside the box resides three other boxes flowing downward that each contain a key/value pair. The upper key reads server with a value of https>//example.com/path/region. The middle key reads timeout with a value of 60. The lower key reads role with a value of Sales.](https://docs-assets.developer.apple.com/published/be561391d727e90169364ad5598d8f39/specifying-and-decoding-a-configuration-2%402x.png)

You design the features that an MDM admin can customize for their deployment. Implement a decoder that parses a configuration based on your specification. To communicate the format to the admin, publish the specification in a place that they can access. The MDM admin configures their unique setup on their MDM server, which delivers the configuration to managed devices.

The device receives a configuration from the server through [`Device Management`](https://developer.apple.com/documentation/DeviceManagement). The MDM admin sets the configuration as needed and triggers the server to send it in the `AppConfig` key (or `ExtensionConfigs`, for app extensions) of an [`AppManaged`](https://developer.apple.com/documentation/DeviceManagement/AppManaged) declaration. [`ManagedApp`](ManagedApp.md) ingests the configuration and passes it to your app after you call [`configurations(_:)`](managedappconfigurationprovider/configurations(_:).md) to provide the framework with your decoder.

![A flow chart with three actors and boxes containing text that represent actions and objects. The actors are, from left to right, App developer, iOS device, and MDM admin. The iOS device actor is split into two inner actors, with the actor at left labeled App and the actor at right labeled ManagedApp framework. Flow begins with three sequential boxes of the App developer actor, which read from top to bottom, Designs configuration specification, Implements decoder class, and Publishes specification. Flow continues to the right to two sequential boxes of the MDM admin actor, which read from top to bottom Reads specification, and Creates or updates configuration. Flow continues to the left to the iOS device actor on the ManagedApp framework side to a box labeled Ingests configuration. To the immediate left in the App column of the iOS device actor resides a box that reads Calls configuration(](https://docs-assets.developer.apple.com/published/0f6cd10d81a0996ca8afec1d510a7f04/specifying-and-decoding-a-configuration-1%402x.png)

The ingestion of a configuration, its decoding, and yielding of a decoded configuration object repeats as the MDM admin provides or updates the configuration at runtime.

> **Note**: Create a configuration decoder to enable the customization of arbitrary properties.  For information about handling secure credentials such as passwords, certificates, and identities, see [`Accessing provisioned secrets with identifiers`](accessing-provisioned-secrets-with-identifiers.md).

#### Design a Configuration Specification

Create a formal specification document for your app’s configuration. You can create a table or use the `appconfig.org` schema. A specification typically includes the following information for every property: key name, value type, whether the property is required, a default value, allowed values, and descriptive text. For example:

| Configuration key name | Type | Required | Default value | Allowed values | Description |
| --- | --- | --- | --- | --- | --- |
| server | string | true | N/A | N/A | The app’s device management server. |
| timeout | integer | false | 60 | N/A | A timeout, in seconds, for the server. |
| role | string | false | staff | sales, marketing, engineering, operations, staff | The person’s job, which can determine that an extra tab displays. |

> ❗ **Important**: When designing your specification, keep the configuration small to facilitate fast transmission. For example, recommend that the MDM admin store any large files that your app needs on an asset server rather than as serialized data in the configuration and include any credentials needed to authenticate their download using a separate network request.

#### Implement a Configuration Decoder

When the device receives your configuration from the server, the framework hands the configuration to your app in the form of a [`Decoder`](https://developer.apple.com/documentation/Swift/Decoder). You author a [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) type that receives the decoder and parses out the properties according to your specification.

Implement a [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) that defines your configuration layout. The following example type holds three custom properties, `server`, `timeout`, and `role`:

```swift
struct MyAppConfiguration: Decodable {
    private(set) var server: String
    private(set) var timeout: Int
    private(set) var role: String
}
```

The decoder requires coding keys to map coded data to your configurable properties. Extend your custom configuration type to add coding keys according to the specification:

```swift
extension MyAppConfiguration {
    enum CodingKeys: String, CodingKey {
        case server
        case timeout
        case role
    }
}
```

Implement an `init(decoder:)` method that ManagedApp uses to receive and parse your configurable properties:

```swift
extension MyAppConfiguration {
    // Initialize your configuration type using info from the server. 
    init(from decoder: Decoder) throws {
        // Decode the configuration using the specified coding keys.  
        let values = try decoder.container(keyedBy: CodingKeys.self)
        // Decode the required `server` value. 
        server = try values.decode(String.self, forKey: .server)
        // Decode the optional `timeout` value. 
        if values.contains(.timeout) {
            timeout = try values.decode(Int.self, forKey: .timeout)
        } else {
            // Set a default timeout if not present. 
            timeout = MyAppConfiguration.defaultTimeout
        }
        // Decode the `role` value. 
        role = try values.decode(String.self, forKey: .role)
    }
}
```

Only decode the incoming configuration in `init(from:)`. The framework enforces a timeout on decoding the configuration by throwing a [`ManagedAppConfigurationDecodingError`](managedappconfigurationdecodingerror.md) with the `timeout` code if your initializer takes too long to complete.

#### Publish Your Configuration Specification

Provide your app’s specification document to MDM admins by storing it in a place they can access, such as by hosting it on your app website. Additionally, you can provide an example configuration that conforms to your specification. The following example property list has the configurable properties, `server`, `timeout`, and `role`:

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>configuration</key>
    <dict>
        <key>server</key>
        <string>https://example.com/path/region</string>
        <key>timeout</key>
        <integer>60</integer>
        <key>role</key>
        <string>sales</string>
    </dict>
</dict>
</plist>
```

The MDM admin sets the values as needed and stores the configuration on the MDM server for communication to managed devices using [`Device Management`](https://developer.apple.com/documentation/DeviceManagement). The MDM server sends the configuration through the `AppConfig` key (or `ExtensionConfigs`, for app extensions) of an [`AppManaged`](https://developer.apple.com/documentation/DeviceManagement/AppManaged) declaration. From the perspective of your app, the device and the [`ManagedApp`](ManagedApp.md) framework obtain your app’s configuration automatically.

#### Access a Configuration Provider and Set Defaults

To supply your app access to the current configuration, implement a class that contains the framework’s configuration provider. For example:

```swift
class MyAppConfigurationProvider {
    // Your app's custom configuration type. 
    private(set) var configuration: MyAppConfiguration
    // An instance of the underlying framework configuration provider. 
    private var configurationProvider: ManagedAppConfigurationProvider
    // Singleton setup. 
    // Enable global access to the configuration.   
    static let shared: MyAppConfigurationProvider = {
        let instance = MyAppConfigurationProvider()
        return instance
    }()
    // Initializes a singleton. 
    private init() {        
        // ... 
    }
}
```

> 💡 **Tip**: Although not required, this example uses a singleton to let you access the configuration globally.

Rely on default values while your app hasn’t yet received a configuration from the server. The following example adds defaults to the custom configuration type:

```swift
extension MyAppConfiguration {
    // A default configuration. 
    static let defaultConfiguration = MyAppConfiguration(
                                        server: defaultServer, 
                                        timeout: defaultTimeout
                                        role: defaultRole)
    // Set default values for configurable properties. 
    static private let defaultServer = "default.example.com"
    static private let defaultTimeout = 60
    static private let defaultRole = "staff"
}
```

Set the default configuration as your app starts, such as during the initialization of your app’s custom configuration provider:

```swift
class MyAppConfigurationProvider {
    // Singleton setup.
    // ...
    // Initializes a singleton. 
    private init() {
        // Start with the defaults. 
        configuration = MyAppConfiguration.defaultConfiguration
        // Initialize the underlying provider.
        configurationProvider = ManagedAppConfigurationProvider()
        // Receive the configuration. 
        // ...
    }
}
```

#### Validate Decoded Values and Throw Decoding Errors

Your configuration type needs to validate the values the admin supplies. Define valid ranges for properties as static additions to your custom type, for example, a lower bound on timeout:

```swift
extension MyAppConfiguration {
    // Range validation. 
    static private let minimumTimeout = 5
}
```

As the decoder parses properties, check that their values are within the expected range.

Let the MDM admin know which values are valid by including allowable ranges in your specification. The following table adds a `minimum value` column to the previous example specification:

| Configuration key name | Type | Required? | Default value | Minimum value | Description |
| --- | --- | --- | --- | --- | --- |
| timeout | integer | false | 60 | 5 | A timeout, in seconds, for the server. |

If `timeout` isn’t in the allowable range, the following `guard` block throws a `MyAppConfigurationDecoderError`, with a specific [`ManagedAppConfigurationDecodingErrorCode`](managedappconfigurationdecodingerrorcode.md).

```swift
guard timeout >= MyAppConfiguration.minimumTimeout else {
    throw MyAppConfigurationDecoderError(code: MyAppConfiguration.timeoutTooLowErrorCode, 
        message: "Timeout \(timeout) is below minimum \(MyAppConfiguration.minimumTimeout).")
}
```

You can define this custom error, for example:

```swift
extension MyAppConfiguration {
    struct MyAppConfigurationDecoderError : ManagedAppConfigurationDecodingError {
        var code: ManagedAppConfigurationDecodingErrorCode
        var message: String
    }
    static let timeoutTooLowErrorCode = ManagedAppConfigurationDecodingErrorCode(rawValue: 100)!
```

#### Document Custom Errors for a Decoding Feedback Loop

Include the errors in your specification so the MDM admin can understand custom error codes. For example, document a code for setting a timeout that’s too low:

| Error name | Code | Description |
| --- | --- | --- |
| timeOutTooLowError | 100 | Server timeout is below the minimum allowed. |

When the decoder finishes, the device reports the decoding results to the MDM server using Device Management [`Status Reports`](https://developer.apple.com/documentation/DeviceManagement/status-reports). On success, the device reports a valid state to the server. If the decoder throws an error and it conforms to [`ManagedAppConfigurationDecodingError`](managedappconfigurationdecodingerror.md), the device provides a status report with an invalid state to the server and logs the error in the device’s event log. The log includes the [`code`](managedappconfigurationdecodingerror/code.md) and [`message`](managedappconfigurationdecodingerror/message.md) properties. If the server receives an invalid state, the MDM admin can request device logs to understand the cause.

If the error doesn’t conform to [`ManagedAppConfigurationDecodingError`](managedappconfigurationdecodingerror.md) or if the error code is reserved, the device reports a generic error.

For more information on status reporting, see [`Leveraging the declarative management data model to scale devices`](https://developer.apple.com/documentation/DeviceManagement/leveraging-the-declarative-management-data-model-to-scale-devices).

> ❗ **Important**: Because the framework logs errors, don’t include sensitive information in error messages.

#### Receive the Configuration and Any Updates

Inside your custom provider’s singleton initializer, receive a configuration:

```swift
Task { /* Configuration provider task */
    for await configuration in configurationProvider.configurations(MyAppConfiguration.self) {
        self.configuration = configuration ?? MyAppConfiguration.defaultConfiguration
    } 
}
```

In the custom configuration provider’s initializer, add the task declaration after setting the default configuration and initializing the custom configuration provider. In the `for await` block, process the new configuration. For example, you can calculate changes in configuration or schedule UI updates in your app.

For the lifetime of the task, the `for await` waits for an updated configuration from the MDM admin and yields the new value as soon as it successfully decodes. If decoding fails, such as if the MDM admin fails to include a required value, the sequence yields `nil`. Keep the task running to watch for changes that the MDM admin makes to the configuration.

> ❗ **Important**: Because the configuration can contain sensitive information, don’t log or displaying decoded portions of the configuration.

#### Apply Configured Values

After your app receives the configuration, it can adjust to the new information. For example if it receives a server URL, your app can request the URL and access the configurable asset or page it refers to. As another example, your app might reveal a Sales tab after learning that the person is a member of the sales team.

![None](https://docs-assets.developer.apple.com/published/4f9ee175d39d73ad7fde21731043b4ba/specifying-and-decoding-a-configuration-3%402x.png)

## See Also

- [class ManagedAppConfigurationProvider](managedappconfigurationprovider.md)
  A class that provides configurations that an MDM admin provisions for a managed app or extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/specifying-and-decoding-a-configuration)*