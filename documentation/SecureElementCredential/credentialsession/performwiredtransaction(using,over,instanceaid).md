# performWiredTransaction(using:over:instanceAID:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Enters wired mode with user authentication.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performWiredTransaction(using credential: CredentialSession.Credential, over scene: UIScene, instanceAID: Data) async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

#### Discussion

If the person using the app chooses to authorize, the specified instance will first have an auth token delivered by the broker interface on the Secure Element as described in the [Apple Business Register](https://register.apple.com) Secure Element documents. Otherwise the session throws `userDeclined`.

Use the following flow to call this method:

1. Call [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) before calling this function to ensure that UI from other applications’ payment tasks don’t interfere with this transaction.
2. Relinquish the asssertion with [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) immediately prior to calling `performWiredTransaction(using:over:instanceAID:)`.
3. After presenting the credential, call [`endWiredMode()`](./endwiredmode%28%29.md) to return to management mode.
4. If you have further proprietary payment UI to perform, use [`acquirePresentmentAssertion()`](./acquirepresentmentassertion%28%29.md) to re-acquire the assertion. Perform your tasks, then call [`relinquish()`](./presentmentintentassertion/relinquish%28%29.md) again. Re-acquiring the assertion is subject to the limit of two assertions in an 80-second span.

The credential session can be in any state when calling this method. If the call succeeds, the state transitions to [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md). The state transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md) if the call encounters a [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md) error; otherwise the state remains unchanged.

An app extension calling this method needs to have the [`Digital Credentials API - Mobile Document Provider`](../../BundleResources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types.md) entitlement.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

> **Throws**: An [`CredentialSession.ErrorCode`](./errorcode.md). The most common errors are:
>
> - [`CredentialSession.ErrorCode.credentialDoesNotExist`](./errorcode/credentialdoesnotexist.md): The specified credential doesn’t exist or the caller doesn’t have access to it.
> - [`CredentialSession.ErrorCode.instanceDoesNotExist`](./errorcode/instancedoesnotexist.md): The specified instance identifier doesn’t exist in the target credential.
> - [`CredentialSession.ErrorCode.userCanceledAuthorization`](./errorcode/usercanceledauthorization.md): The user dismissed the authorization sheet.
> - [`CredentialSession.ErrorCode.resourceUnavailable`](./errorcode/resourceunavailable.md): The system resource is unavailable. The session transitions to [`CredentialSession.State.management`](./state-swift.enum/management.md).

## Parameters

- `credential`: The credential to activate and transition into card emulation state with.
- `scene`: The [`UIScene`](../../UIKit/uiscene.md) the authentication sheet appears over.
- `instanceAID`: The applet instance identifier of the installed credential to authorize.

## See Also

### Performing wired mode actions
- [func enterWiredMode(using: CredentialSession.Credential) async throws](./enterwiredmode%28using%29.md)
  Enters wired mode to perform maintenance operations with the given credential.
- [func transceive(Data) async throws -> Data](./transceive%28_%29.md)
  Send a wired command Application Protocol Data Unit (APDU) to the credential to complete a transaction or a card content management task.
- [func endWiredMode() async throws](./endwiredmode%28%29.md)
  Ends wired mode and returns to management state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/performwiredtransaction(using:over:instanceaid:))*