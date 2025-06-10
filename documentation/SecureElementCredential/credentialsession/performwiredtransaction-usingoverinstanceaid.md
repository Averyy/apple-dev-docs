# performWiredTransaction(using:over:instanceAID:)

**Framework**: SecureElementCredential  
**Kind**: method

Enters wired mode with user authentication.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performWiredTransaction(using credential: CredentialSession.Credential, over scene: UIScene, instanceAID: Data) async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

If the user chooses to authorize, the specified instance will first have an auth token delivered by the broker interface on the Secure Element as described in the [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com) Secure Element documents. Otherwise the session throws `userDeclined`.

Use the following flow to call this method:

1. Call [`acquirePresentmentAssertion()`](credentialsession/acquirepresentmentassertion().md) before calling this function to ensure that UI from other applications’ payment tasks don’t interfere with this transaction.
2. Relinquish the asssertion with [`relinquish()`](credentialsession/presentmentintentassertion/relinquish().md) immediately prior to calling `performWiredTransaction(using:over:instanceAID:)`.
3. After presenting the credential, call [`endWiredMode()`](credentialsession/endwiredmode().md) to return to management mode.
4. If you have further proprietary payment UI to perform, use [`acquirePresentmentAssertion()`](credentialsession/acquirepresentmentassertion().md) to re-acquire the assertion. Perform your tasks, then call [`relinquish()`](credentialsession/presentmentintentassertion/relinquish().md) again. Re-acquiring the assertion is subject to the limit of two assertions in an 80-second span.

The credential session can be in any state when calling this method. If the call succeeds, the state transitions to [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md). The state transitions to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

## Parameters

- `credential`: The credential to activate and transition into card emulation state with.
- `scene`: The   the authentication sheet appears over.
- `instanceAID`: The applet instance identifier of the installed credential to authorize.

## See Also

- [func enterWiredMode(using: CredentialSession.Credential) async throws](credentialsession/enterwiredmode(using:).md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func transceive(Data) async throws -> Data](credentialsession/transceive(_:).md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential.
- [func endWiredMode() async throws](credentialsession/endwiredmode.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/performwiredtransaction(using:over:instanceaid:))*