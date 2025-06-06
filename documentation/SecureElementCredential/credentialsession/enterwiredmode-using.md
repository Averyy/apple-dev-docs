# enterWiredMode(using:)

**Framework**: SecureElementCredential  
**Kind**: method

Enters wired mode to perform maintenance operations with the given credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func enterWiredMode(using credential: CredentialSession.Credential) async throws
```

#### Discussion

You can call this method in any session state. If successful, the state transitions to [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md). The state transitions to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

## Parameters

- `credential`: The installed credential with which to enter wired mode.

## See Also

- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](credentialsession/performwiredtransaction(using:over:instanceaid:).md)
  Enters wired mode with user authentication.
- [func transceive(Data) async throws -> Data](credentialsession/transceive(_:).md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential.
- [func endWiredMode() async throws](credentialsession/endwiredmode.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/enterwiredmode(using:))*