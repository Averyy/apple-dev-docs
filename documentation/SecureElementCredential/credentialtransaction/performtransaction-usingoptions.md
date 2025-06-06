# performTransaction(using:options:)

**Framework**: SecureElementCredential  
**Kind**: method

Prompts the user for authorization and then activates a credential for card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performTransaction(using credential: Credential, options: CardEmulationOptions = .init()) async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

If this call succeeds, the session state trasitions to [`CredentialSession.State.cardEmulation(credential:)`](credentialsession/state-swift.enum/cardemulation(credential:).md), and the event stream publishes a [`CredentialSession.Event.fieldStateChanged(info:)`](credentialsession/event/fieldstatechanged(info:).md) event.

Card emulation ends after 60 seconds, at which point the the event stream publishes a [`CredentialSession.Event.cardEmulationTimeout`](credentialsession/event/cardemulationtimeout.md) event. If you complete your transaction before the timeout, call [`endCardEmulation()`](credentialsession/endcardemulation().md) to exit card emulation mode.

The caller needs to invoke [`invalidate()`](credentialtransaction/configuration/invalidate().md) after completing each transaction.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

Calling this method may generate a billable event to the credential provider.

## Parameters

- `credential`: The credential to activate and transition into card emulation state.
- `options`: The options to activate the credential with, defaults to none.

## See Also

- [func performTransactionInWiredMode(using: Credential, instanceAID: Data) async throws](credentialtransaction/performtransactioninwiredmode(using:instanceaid:).md)
  Enters wired mode to perform a transaction.
- [func performCardEmulationTransactionWithCurrentCredential(options: CardEmulationOptions) async throws](credentialtransaction/performcardemulationtransactionwithcurrentcredential(options:).md)
  Activate the current credential to perform a transaction in card emulation mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/performtransaction(using:options:))*