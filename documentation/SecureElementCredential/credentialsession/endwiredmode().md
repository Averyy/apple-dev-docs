# endWiredMode()

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Ends wired mode and returns to management state.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func endWiredMode() async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

The credential session state must be [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md) prior to calling this method.

## See Also

### Performing wired mode actions
- [func performWiredTransaction(using: CredentialSession.Credential, over: UIScene, instanceAID: Data) async throws](./performwiredtransaction%28using,over,instanceaid%29.md)
  Enters wired mode with user authentication.
- [func enterWiredMode(using: CredentialSession.Credential) async throws](./enterwiredmode%28using%29.md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func transceive(Data) async throws -> Data](./transceive%28_%29.md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential to complete a transaction or a card content management task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/endwiredmode())*