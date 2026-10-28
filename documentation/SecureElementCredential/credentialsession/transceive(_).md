# transceive(_:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Send a wired command Application Protocol Data Unit (APDU) to the credential to complete a transaction or a card content management task.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func transceive(_ data: Data) async throws -> Data
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Return Value

A response APDU.

## Discussion

Before calling this method, make sure the credential session state is [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md). The state transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

Use this method to perform the web presentment transaction after calling `performWiredTransaction(using:over:instanceaid:)`.

> **Note**: When performing a [`transceive(_:)`](./transceive%28_%29.md) call, the system grants your app a 15-second grace period from invalidating the session, in the event your app goes into the background.

- The most common errors are:

  - [`CredentialSession.ErrorCode.invalidSessionState`](./errorcode/invalidsessionstate.md): The session isn’t in the [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md) state.
  - [`CredentialSession.ErrorCode.commandNotSupported`](./errorcode/commandnotsupported.md): The APDU represents an unsupported Secure Element command.
  - [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md): The system resource is unavailable. The session transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md).
  - [`CredentialSession.ErrorCode.acquiredResourceRelinquished`](./errorcode/acquiredresourcerelinquished.md): The shared system resource was relinquished during the operation.

## Parameters

- `data`: The APDU as a [`Data`](../../Foundation/data.md) instance.

## See Also

### Performing wired mode actions
- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](./performwiredtransaction%28using,over,instanceaid%29.md)
  Enters wired mode with user authentication.
- [func enterWiredMode(using: CredentialSession.Credential) async throws](./enterwiredmode%28using%29.md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func endWiredMode() async throws](./endwiredmode%28%29.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/transceive(_:))*