# performCardEmulationTransactionWithCurrentCredential(options:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Activate the current credential to perform a transaction in card emulation mode.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performCardEmulationTransactionWithCurrentCredential(options: CardEmulationOptions = .init()) async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

Calling this method requires that the credential’s state is `wired`. If successful, the state transitions to [`CredentialSession.State.cardEmulation(credential:)`](../credentialsession/state-swift.enum/cardemulation%28credential%29.md). If an error occurs, the state is unchanged, unless the error is [`CredentialSession.ErrorCode.resourceUnavailable`](../credentialsession/errorcode/resourceunavailable.md), which transitions the state back to [`CredentialSession.State.management`](../credentialsession/state-swift.enum/management.md).

When you call this method, the following sequence of events takes place:

1. The system prompts the user to authorize Card Emulation.
2. The system deselects the instance on the wired interface.
3. The system calls the broker interface with authorization information, if applicable. See the integration guide in the [Apple Business Register](https://register.apple.com).
4. The system makes the instance available over the contactless interface and transitions the session to the card emulation state.

This process is guaranteed to preserve contents of the Clear On Reset buffer in the operating system running on the Secure Element. This allows you to create some context in wired mode that remains valid later in card emulation mode.

The caller needs to invoke [`invalidate()`](./configuration/invalidate%28%29.md) after completing each transaction.

> ❗ **Important**: Calling this method may generate a billable event to the credential provider.

> **Throws**: An [`CredentialSession.ErrorCode`](../credentialsession/errorcode.md). The most common errors are:
>
> - [`CredentialSession.ErrorCode.invalidView`](../credentialsession/errorcode/invalidview.md): The transaction has no associated scene.
> - [`CredentialSession.ErrorCode.userCanceledAuthorization`](../credentialsession/errorcode/usercanceledauthorization.md): The user dismissed the authorization sheet.
> - [`CredentialSession.ErrorCode.resourceUnavailable`](../credentialsession/errorcode/resourceunavailable.md): The system resource is unavailable.

## Parameters

- `options`: The options to transition the credential to card emulation mode.

## See Also

### Performing transactions
- [func performTransaction(using: Credential, options: CardEmulationOptions) async throws](./performtransaction%28using,options%29.md)
  Prompts the user for authorization and then activates a credential for card emulation.
- [func performTransactionInWiredMode(using: Credential, instanceAID: Data) async throws](./performtransactioninwiredmode%28using,instanceaid%29.md)
  Enters wired mode to perform a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/performcardemulationtransactionwithcurrentcredential(options:))*