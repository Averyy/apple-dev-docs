# CredentialSession.CardEmulationOptions

**Framework**: SecureElementCredential  
**Kind**: struct  
**Role**: Structure

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
- [init()](./cardemulationoptions/init%28%29.md)
  Creates a card emulation options instance.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing card emulation
- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./performcardemulationtransactionwithcurrentcredential%28over,options%29.md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [func performTransaction(using: CredentialSession.Credential, over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./performtransaction%28using,over,options%29.md)
  Prompts the user for authorization and then activate a credential for card emulation.
- [func endCardEmulation() async throws](./endcardemulation%28%29.md)
  Ends card emulation and transitions the session to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/cardemulationoptions)*