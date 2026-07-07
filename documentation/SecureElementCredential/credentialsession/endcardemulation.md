# endCardEmulation()

**Framework**: SecureElementCredential  
**Kind**: method

Ends card emulation and transitions the session to management state.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func endCardEmulation() async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

## See Also

- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](credentialsession/performcardemulationtransactionwithcurrentcredential(over:options:).md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [func performTransaction(using: CredentialSession.Credential, over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](credentialsession/performtransaction(using:over:options:).md)
  Prompts the user for authorization and then activate a credential for card emulation.
- [CredentialSession.CardEmulationOptions](credentialsession/cardemulationoptions.md)
  Options for customizing card emulation behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/endcardemulation())*