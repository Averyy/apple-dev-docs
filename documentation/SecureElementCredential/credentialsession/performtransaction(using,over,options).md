# performTransaction(using:over:options:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Prompts the user for authorization and then activate a credential for card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performTransaction(using credential: CredentialSession.Credential, over scene: UIScene, options: CredentialSession.CardEmulationOptions = .init()) async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

1. Call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) before calling this function to ensure that UI from other applications’ payment tasks don’t interfere with this transaction.
2. Relinquish the asssertion with [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) immediately prior to calling `performTransaction(using:over:options:)`.
3. After presenting the credential, call [`endCardEmulation()`](./endcardemulation%28%29.md) to return to management mode.
4. If you have further proprietary payment UI to perform, use [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) to re-acquire the assertion. Perform your tasks, then call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) again. Re-acquiring the assertion is subject to the limit of two assertions in an 80-second span.

The credential session state must be [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md) prior to calling this method. The state transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

If this call succeeds the credential session state transitions to the [`CredentialSession.State.cardEmulation(credential:)`](./state-swift.enum/cardemulation%28credential%29.md) state.

If not ended sooner, card emulation expires after 60 seconds and the credential session publishes a [`CredentialSession.Event.cardEmulationTimeout`](./event/cardemulationtimeout.md) event.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

> **Throws**: An [`CredentialSession.ErrorCode`](./errorcode.md). The most common errors are:
>
> - [`CredentialSession.ErrorCode.userCanceledAuthorization`](./errorcode/usercanceledauthorization.md): The user dismissed the authorization sheet.
> - [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md): The system resource is unavailable. The session transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md).

## Parameters

- `credential`: The credential to activate and transition into card emulation state with.
- `scene`: The [`UIScene`](../../UIKit/uiscene.md) the authentication sheet appears over.
- `options`: Options with which to transition the credential to card emulation mode.

## See Also

### Performing card emulation
- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](./performcardemulationtransactionwithcurrentcredential%28over,options%29.md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [CredentialSession.CardEmulationOptions](./cardemulationoptions.md)
  Options for customizing card emulation behavior.
- [func endCardEmulation() async throws](./endcardemulation%28%29.md)
  Ends card emulation and transitions the session to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/performtransaction(using:over:options:))*