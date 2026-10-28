# enterWiredMode(using:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Enters wired mode to perform maintenance operations with the given credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func enterWiredMode(using credential: CredentialSession.Credential) async throws
```

## Discussion

You can call this method in any session state. If successful, the state transitions to [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md). The state transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

- The most common errors are:

  - [`CredentialSession.ErrorCode.invalidCredentialState`](./errorcode/invalidcredentialstate.md): The credential isn’t in the [`CredentialSession.Credential.State.installed(instances:)`](./credential/state-swift.enum/installed%28instances%29.md) state.
  - [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md): The system resource is unavailable. The session transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md).

## Parameters

- `credential`: The installed credential with which to enter wired mode.

## See Also

### Performing wired mode actions
- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](./performwiredtransaction%28using,over,instanceaid%29.md)
  Enters wired mode with user authentication.
- [func transceive(Data) async throws -> Data](./transceive%28_%29.md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential to complete a transaction or a card content management task.
- [func endWiredMode() async throws](./endwiredmode%28%29.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/enterwiredmode(using:))*