# performTransaction(using:options:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Prompts the user for authorization and then activates a credential for card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performTransaction(using credential: Credential, options: CardEmulationOptions = .init()) async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

If this call succeeds, the session state trasitions to [`CredentialSession.State.cardEmulation(credential:)`](../credentialsession/state-swift.enum/cardemulation%28credential%29.md).

Card emulation ends after 60 seconds, at which point the the event stream publishes a [`CredentialSession.Event.cardEmulationTimeout`](../credentialsession/event/cardemulationtimeout.md) event. If you complete your transaction before the timeout, call [`endCardEmulation()`](../credentialsession/endcardemulation%28%29.md) to exit card emulation mode.

The caller needs to invoke [`invalidate()`](./configuration/invalidate%28%29.md) after completing each transaction.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

> **Throws**: An [`CredentialSession.ErrorCode`](../credentialsession/errorcode.md). The most common errors are:
>
> - [`CredentialSession.ErrorCode.invalidView`](../credentialsession/errorcode/invalidview.md): The transaction has no associated scene.
> - [`CredentialSession.ErrorCode.userCanceledAuthorization`](../credentialsession/errorcode/usercanceledauthorization.md): The user dismissed the authorization sheet.
> - [`CredentialSession.ErrorCode.resourceUnavailable`](../credentialsession/errorcode/resourceunavailable.md): The system resource is unavailable.

## Parameters

- `credential`: The credential to activate and transition into card emulation state.
- `options`: The options to activate the credential with, defaults to none.

## See Also

### Performing transactions
- [func performTransactionInWiredMode(using: Credential, instanceAID: Data) async throws](./performtransactioninwiredmode%28using,instanceaid%29.md)
  Enters wired mode to perform a transaction.
- [func performCardEmulationTransactionWithCurrentCredential(options: CardEmulationOptions) async throws](./performcardemulationtransactionwithcurrentcredential%28options%29.md)
  Activate the current credential to perform a transaction in card emulation mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/performtransaction(using:options:))*