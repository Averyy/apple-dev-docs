# performTransaction(using:over:options:)

**Framework**: SecureElementCredential  
**Kind**: method

Prompts the user for authorization and then activate a credential for card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performTransaction(using credential: CredentialSession.Credential, over scene: UIScene, options: CredentialSession.CardEmulationOptions = .init()) async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

1. Call [`acquirePresentmentAssertion()`](credentialsession/acquirepresentmentassertion().md) before calling this function to ensure that UI from other applications’ payment tasks don’t interfere with this transaction.
2. Relinquish the asssertion with [`relinquish()`](credentialsession/presentmentintentassertion/relinquish().md) immediately prior to calling `performTransaction(using:over:options:)`.
3. After presenting the credential, call [`endCardEmulation()`](credentialsession/endcardemulation().md) to return to management mode.
4. If you have further proprietary payment UI to perform, use [`acquirePresentmentAssertion()`](credentialsession/acquirepresentmentassertion().md) to re-acquire the assertion. Perform your tasks, then call [`relinquish()`](credentialsession/presentmentintentassertion/relinquish().md) again. Re-acquiring the assertion is subject to the limit of two assertions in an 80-second span.

The credential session state must be [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md) prior to calling this method. The state transitions to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

If this call succeeds the credential session state transitions to the [`CredentialSession.State.cardEmulation(credential:)`](credentialsession/state-swift.enum/cardemulation(credential:).md) state. The session also publishes a [`CredentialSession.Event.fieldStateChanged(info:)`](credentialsession/event/fieldstatechanged(info:).md) event.

If not ended sooner, card emulation expires after 60 seconds and the credential session publishes a [`CredentialSession.Event.cardEmulationTimeout`](credentialsession/event/cardemulationtimeout.md) event.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

## Parameters

- `credential`: The credential to activate and transition into card emulation state with.
- `scene`: The   the authentication sheet appears over.
- `options`: Options with which to transition the credential to card emulation mode.

## See Also

- [func performCardEmulationTransactionWithCurrentCredential(over: UIScene, options: CredentialSession.CardEmulationOptions) async throws](credentialsession/performcardemulationtransactionwithcurrentcredential(over:options:).md)
  Activate the current credential in Wired mode to enter Card Emulation mode.
- [CredentialSession.CardEmulationOptions](credentialsession/cardemulationoptions.md)
  Options for customizing card emulation behavior.
- [func endCardEmulation() async throws](credentialsession/endcardemulation.md)
  Ends card emulation and transitions the session to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/performtransaction(using:over:options:))*