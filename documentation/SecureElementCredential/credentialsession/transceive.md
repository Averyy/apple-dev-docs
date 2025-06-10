# transceive(_:)

**Framework**: SecureElementCredential  
**Kind**: method

Send a wired command Application Protocol Data Unit (APDU) to the credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func transceive(_ data: Data) async throws -> Data
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Return Value

A response APDU.

#### Discussion

Before calling this method, make sure the credential session state is [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md). The state transitions to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

> **Note**: When performing a [`transceive(_:)`](credentialsession/transceive(_:).md) call, the system grants your app a 15-second grace period from invalidating the session, in the event your app goes into the background.

## Parameters

- `data`: The APDU as a   instance.

## See Also

- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](credentialsession/performwiredtransaction(using:over:instanceaid:).md)
  Enters wired mode with user authentication.
- [func enterWiredMode(using: CredentialSession.Credential) async throws](credentialsession/enterwiredmode(using:).md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func endWiredMode() async throws](credentialsession/endwiredmode.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/transceive(_:))*