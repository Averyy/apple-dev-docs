# endWiredMode()

**Framework**: SecureElementCredential  
**Kind**: method

Ends wired mode and returns to management state.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func endWiredMode() async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

The credential session state must be [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md) prior to calling this method.

## See Also

- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](credentialsession/performwiredtransaction(using:over:instanceaid:).md)
  Enters wired mode with user authentication.
- [func enterWiredMode(using: CredentialSession.Credential) async throws](credentialsession/enterwiredmode(using:).md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func transceive(Data) async throws -> Data](credentialsession/transceive(_:).md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/endwiredmode())*