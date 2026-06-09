# Integrating declarative management

**Framework**: Device Management

Use declarative management to deploy configurations and retrieve status updates more efficiently.

#### Overview

The declarations and the status channels of declarative management can coexist with MDM commands and profiles, which means you can gradually adopt the new features, without having to update all device management workflows at once. For example, a device management service might just implement status subscriptions to effectively add a status channel to the MDM protocol without having to adopt all of declarative management.

Importantly, this integration doesn’t interfere with existing MDM behavior. Declarative management has to be explicitly enabled with a new MDM command, before you can use any of its features. Without that enablement, the MDM protocol functions exactly as before.

#### Enable Declarative Management

The device management service enables declarative management by sending a [`DeclarativeManagementCommand`](declarativemanagementcommand.md) to the device through the usual MDM command processing flow. This command serves two purposes:

- It enables the declarative management features.
- It signals to the device that the device management service has updated declarations and the device needs synchronize the declarations with the service. In this case, the command can include a payload containing synchronization tokens to allow for an efficient synchronization flow.

After your device management service has turned on declarative management, it can’t be turned off. However, the service can remove all declarations from the device to effectively turn off any declarative management behavior.

If you unenroll a device, the device removes all declarative management state, including all policies applied through declarations.

> **Note**:  On macOS and Shared iPad, you must send the management commands separately on the device and user channels to turn on declarative management on each channel. Similarly, each channel reports declarative management status separately.

#### Synchronize Declarative Management

Synchronize declarations by following these steps:

1. The device management service sends a device management push notification to the device.
2. The device responds to the push in the usual manner by requesting the next MDM command from the device management service.
3. The service responds with a [`DeclarativeManagementCommand`](declarativemanagementcommand.md) that should include the [`SynchronizationTokens`](synchronizationtokens.md) JSON data.
4. The device checks the `DeclarationsToken` in the `SyncTokens` sent in the command.
5. The device fetches the declarations manifest from the device management service.
6. The device synchronizes changes.

The next sections describe the synchronization details in steps 4-6 in more detail.

#### Check Synchronization Tokens

The device management service maintains a token that represents the current state of the declarations to synchronize with a particular device. The service must persist this token on a per-device and per-user basis because declarations may be different for some devices and some users. Whenever the set of declarations changes (new ones added or existing ones changed or removed), the service must change the value of the token. The token value is an opaque string that the client uses for comparisons, so the service is free to use whatever format it prefers, but needs to limit the size to no more that 256 octets.

The device management service can send the token to the device as the `DeclarationsToken` item in the command’s `Data` key. The service also sends the token to the device in the service’s declarations manifest response, along with the data for the set of declarations it applies to.

When the client processes the service’s declarations manifest, it persists the declarations token that the service sends. The device uses that value to determine whether it needs to update the declarations manifest. When the device receives a [`DeclarativeManagementCommand`](declarativemanagementcommand.md) command, it initiates a synchronization operation that uses the following rules to determine what steps to take:

- If the [`DeclarativeManagementCommand`](declarativemanagementcommand.md) doesn’t contain a `Data` key, the device fetches the current set of synchronization tokens from the device management service with a [`Declarative Management`](declarative-management.md) `tokens` `Endpoint` request. It then uses the `DeclarationsToken` key extracted from the service’s response.
- If the [`DeclarativeManagementCommand`](declarativemanagementcommand.md) contains a `Data` key, the device extracts the value of the `DeclarationsToken`.

The device compares the new declaration token to the last declaration token received from the device management service:

- If the new and existing tokens match, the device assumes the declarations of the device management service are identical since the last synchronization, and the current synchronization operation ends.
- If the new and existing tokens don’t match, the device continues the synchronization operation by fetching the declarations manifest from the device management service with a [`Declarative Management`](declarative-management.md) `declaration-items` `Endpoint` request. The declaration manifest is a JSON object with keys for each declaration type, whose values are an array of declaration item descriptors. Those descriptors contain the Identifier and `ServerToken` values for each declaration for the device to synchronize.

#### Synchronize Device State

The device uses the declaration items in the declaration manifest to synchronize its state with the device management service using the following logic:

- If the declaration manifest contains a declaration item with an `Identifier` that doesn’t match the `Identifier` of any declaration present on the device, the device considers that to be a new declaration, and fetches it with a [`Declarative Management`](declarative-management.md) declaration Endpoint request.
- If the declaration manifest contains a declaration item with an `Identifier` that does match the `Identifier` of a declaration present on the device and the `ServerToken` items don’t match, the device considers that to be an updated declaration, and fetches it with a [`Declarative Management`](declarative-management.md) declaration Endpoint request.

After processing the entire declaration manifest, if there are declarations present on the device with an `Identifier` that isn’t present in the declaration manifest, the device marks those declarations for removal.

After processing the declaration manifest, and fetching any new or changed declarations, the device removes all declarations marked for removal, and then updates its state by applying the new and changed declarations, and un-applying the removed declarations.

#### Download Asset Data

Some asset declarations contain a `Reference` which in turn contains a `DataURL` that specifies the URL where the corresponding asset data resides. The device treats this URL as hosted by the device management service and applies normal MDM protocol rules to the request. There are additional keys in the `Reference` key that the system uses to verify the integrity of the downloaded asset data. The device procedure for fetching and verifying the data is:

1. The device uses a TLS connection with a client certificate set to the device’s’ identity certificate.
2. The device verifies the TLS certificate of the device management service by evaluating trust with any `CheckInURLPinningCertificateUUIDs` specified in the device management (MDM) enrollment profile payload. In this case, the device honors the `PinningRevocationCheckRequired` specified in the device management (MDM) enrollment profile payload.
3. The device verifies that the HTTP response `Content-Type` header specifies a media type that matches the value of the `ContentType` in the `Reference` of the asset. If the media type values don’t match, the asset data download fails.
4. The device verifies that the size of the downloaded data in bytes, matches the value of the `Size` in the `Reference` of the asset. If the sizes don’t match, the asset data download fails.
5. The device verifies that the SHA-256 hash of the downloaded data, matches the value of the Hash-SHA-256 key in the `Reference` of the asset. If the hash values don’t match, the asset data download fails.

The `com.apple.configuration.legacy` and `com.apple.configuration.legacy.interactive` configurations both contain a `ProfileURL` key that specifies the URL where the corresponding profile data resides. The device considers this URL hosted by the device management service and applies normal MDM protocol rules to the request. In particular:

1. The device uses a TLS connection with a client certificate set to the device’s’ identity certificate.
2. The device verifies the TLS certificate of the device management service by evaluating trust with any `CheckInURLPinningCertificateUUIDs` specified in the device management (MDM) enrollment profile payload. In this case, the device honors the `PinningRevocationCheckRequired` specified in the device management (MDM) enrollment profile payload.

## See Also

- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)
  Use declarative management to make devices more autonomous and proactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/integrating-declarative-management)*