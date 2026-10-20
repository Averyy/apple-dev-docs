# endCardEmulation()

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Ends card emulation and transitions the session to management state.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func endCardEmulation() async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## See Also

### Performing card emulation
- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./performcardemulationtransactionwithcurrentcredential%28over,options%29.md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [func performTransaction(using: CredentialSession.Credential, over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./performtransaction%28using,over,options%29.md)
  Prompts the user for authorization and then activate a credential for card emulation.
- [CredentialSession.CardEmulationOptions](./cardemulationoptions.md)
  Options for customizing card emulation behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/endcardemulation())*