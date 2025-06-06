# Setting up the HTTP endpoints for Live Caller ID Lookup

**Framework**: SMS and Call Reporting

Connect the on-device system to your server.

#### Overview

For the Live Caller ID Lookup extension, your client-side app needs your [`serviceURL`](livecalleridlookupextensioncontext/serviceurl.md) so the system can fetch information from your server. Communication between the system and the server uses protocol buffer messages over HTTP. For more information, see [`Homomorphic Encryption Protobuf`](https://developer.apple.comhttps://github.com/apple/swift-homomorphic-encryption-protobuf).

Implement your server with the following HTTP endpoints:

- `/config`
- `/key`
- `/queries`

##### Get Configuration and Status

The system calls the configuration endpoint periodically to get information about the use case configuration and evaluation key status. Set up the following `/config` endpoint by posting to `/config`:

| Request | Value | Description |
| --- | --- | --- |
| Header | `User-Identifier` | A pseudorandom identifier for the user. |
| Header | `Authorization` | The value that contains a private access token. |
| Request body | `ConfigRequest` | A serialized protocol buffer message. |
| Response | `ConfigResponse` | A serialized protocol buffer message. The `ConfigResponse` contains the `configs` and `key_info` response fields. |
| Response field | `configs` | A field that maps from the use case names to the corresponding configuration. |
| Response field | `key_info` | A list of the `KeyStatus` objects. |

##### Upload the Evaluation Key

You store the evaluation key on your server. When the system detects a new evaluation key, it uses the `/key` endpoint to upload it. Set up the following `/key` endpoint to upload an evaluation key by posting to `/key`:

| Request | Value | Description |
| --- | --- | --- |
| Header | `User-Identifier` | A pseudorandom identifier for the user. |
| Header | `Authorization` | The value that contains a private access token. |
| Request body | `EvaluationKeys` | A serialized protocol buffer message. |

##### Update Pir Requests

The system updates your private information retrieval (PIR) request through the `/queries` endpoint. Set up the `/queries` endpoint to evaluate PIR requests.

| Request | Value | Description |
| --- | --- | --- |
| Header | `User-Identifier` | A pseudorandom identifier for the user. This value looks up the previously stored evaluation key and uses it to evaluate the PIR request. |
| Header | `Authorization` | The value that contains a private access token. |
| Request body | `Requests` | A serialized protocol buffer message. |
| Response | `Responses` | A serialized protocol buffer message. |

## See Also

- [Understanding how Live Caller ID Lookup preserves privacy](understanding-how-live-caller-id-lookup-preserves-privacy.md)
  Use Live Caller ID Lookup to protect user privacy by hiding the client’s IP address, using anonymous authentication, and hiding the incoming phone number.
- [Formatting data for blocking and identity information](formatting-data-for-blocking-and-identity-information.md)
  Set up your PIR payload for call blocking and identity information.
- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)
  Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
- [protocol LiveCallerIDLookupProtocol](livecalleridlookupprotocol.md)
  Information the system uses to query the app extension for context.
- [protocol LiveCallerIDLookupExtensionConfiguration](livecalleridlookupextensionconfiguration.md)
  An object that allows the system to query the app extension.
- [struct LiveCallerIDLookupExtensionContext](livecalleridlookupextensioncontext.md)
  The information the system uses for configuration.
- [enum CallLookupExtensionStatus](calllookupextensionstatus.md)
  Returns a value with the current state of the app extension.
- [class LiveCallerIDLookupManager](livecalleridlookupmanager.md)
  The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/setting-up-the-http-endpoints-for-live-caller-id-lookup)*