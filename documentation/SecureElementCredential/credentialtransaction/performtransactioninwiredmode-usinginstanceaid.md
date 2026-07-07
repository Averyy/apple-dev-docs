# performTransactionInWiredMode(using:instanceAID:)

**Framework**: SecureElementCredential  
**Kind**: method

Enters wired mode to perform a transaction.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func performTransactionInWiredMode(using credential: Credential, instanceAID: Data) async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

After you call this method, the system shows an authorization screen to the person using the app. If they choose to authorize, the specified instance receives an authentication token. The instance receives this token through the broker interface on the Secure Element as described in the [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login) Secure Element documents.

If the person using the app declines the authorization, the session throws [`CredentialSession.ErrorCode.accessDenied`](credentialsession/errorcode/accessdenied.md).

You can call this method in any session state. The state transitions to [`CredentialSession.State.wired(credential:)`](credentialsession/state-swift.enum/wired(credential:).md) if successful. If an error occurs, the state is unchanged, unless the error is [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md), which transitions the state back to [`CredentialSession.State.management`](credentialsession/state-swift.enum/management.md).

The caller must invoke [`invalidate()`](credentialtransaction/configuration/invalidate().md) after completing each transaction.

> **Note**: An [`CredentialSession.ErrorCode`](credentialsession/errorcode.md). The most common errors are: - [`CredentialSession.ErrorCode.invalidView`](credentialsession/errorcode/invalidview.md): The transaction has no associated scene.
- [`CredentialSession.ErrorCode.credentialDoesNotExist`](credentialsession/errorcode/credentialdoesnotexist.md): The specified credential doesn’t exist or the caller doesn’t have access to it.
- [`CredentialSession.ErrorCode.instanceDoesNotExist`](credentialsession/errorcode/instancedoesnotexist.md): The specified instance identifier doesn’t exist in the target credential.
- [`CredentialSession.ErrorCode.userCanceledAuthorization`](credentialsession/errorcode/usercanceledauthorization.md): The user dismissed the authorization sheet.
- [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md): The system resource is unavailable.

## Parameters

- `credential`: The installed credential to enter wired mode with.
- `instanceAID`: The instance applet instance identifier of the installed credential to authorize.

## See Also

- [func performTransaction(using: Credential, options: CardEmulationOptions) async throws](credentialtransaction/performtransaction(using:options:).md)
  Prompts the user for authorization and then activates a credential for card emulation.
- [func performCardEmulationTransactionWithCurrentCredential(options: CardEmulationOptions) async throws](credentialtransaction/performcardemulationtransactionwithcurrentcredential(options:).md)
  Activate the current credential to perform a transaction in card emulation mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction/performtransactioninwiredmode(using:instanceaid:))*