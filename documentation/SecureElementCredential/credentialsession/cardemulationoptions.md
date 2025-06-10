# CredentialSession.CardEmulationOptions

**Framework**: SecureElementCredential  
**Kind**: struct

Options for customizing card emulation behavior.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
struct CardEmulationOptions
```

## Topics

### Creating an options instance
- [init()](credentialsession/cardemulationoptions/init.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](credentialsession/performcardemulationtransactionwithcurrentcredential(over:options:).md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [func performTransaction(using: CredentialSession.Credential, over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](credentialsession/performtransaction(using:over:options:).md)
  Prompts the user for authorization and then activate a credential for card emulation.
- [func endCardEmulation() async throws](credentialsession/endcardemulation.md)
  Ends card emulation and transitions the session to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/cardemulationoptions)*