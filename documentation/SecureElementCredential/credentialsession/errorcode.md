# CredentialSession.ErrorCode

**Framework**: SecureElementCredential  
**Kind**: enum

An error encountered by a credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum ErrorCode
```

## Topics

### Authorization and permission error codes
- [CredentialSession.ErrorCode.userNotAuthorized](credentialsession/errorcode/usernotauthorized.md)
  The person using the app isn’t authorized to perform the operation.
- [CredentialSession.ErrorCode.accessDenied](credentialsession/errorcode/accessdenied.md)
  The person using the app declined to grant permission for the operation.
- [CredentialSession.ErrorCode.clientNotInForeground](credentialsession/errorcode/clientnotinforeground.md)
  Your app isn’t in the foreground, which is required to use the credential session.
- [CredentialSession.ErrorCode.userCanceledAuthorization](credentialsession/errorcode/usercanceledauthorization.md)
  The person using the app dismissed the authorization sheet.
- [CredentialSession.ErrorCode.userAuthorizationTimedOut](credentialsession/errorcode/userauthorizationtimedout.md)
  Authorization timed out while waiting for the person using the app.
- [CredentialSession.ErrorCode.featureUnavailable](credentialsession/errorcode/featureunavailable.md)
  The feature is unavailable.
- [CredentialSession.ErrorCode.ineligible](credentialsession/errorcode/ineligible.md)
  The current device and user configuation are ineligible to use this service.
- [CredentialSession.ErrorCode.conditionsNotSatisfied](credentialsession/errorcode/conditionsnotsatisfied.md)
  The iCloud account or passcode of the person using the app don’t satisfy the conditions to use this service.
### Credential error codes
- [CredentialSession.ErrorCode.invalidCredentialState](credentialsession/errorcode/invalidcredentialstate.md)
  A credential is in a state that doesn’t permit that function.
- [CredentialSession.ErrorCode.credentialDoesNotExist](credentialsession/errorcode/credentialdoesnotexist.md)
  The credential doesn’t exist, or you don’t have access to it.
- [CredentialSession.ErrorCode.instanceDoesNotExist](credentialsession/errorcode/instancedoesnotexist.md)
  The instance doesn’t exist in the target credential.
### Session error codes
- [CredentialSession.ErrorCode.invalidSessionState](credentialsession/errorcode/invalidsessionstate.md)
  The session is in a state that doesn’t permit that function.
- [CredentialSession.ErrorCode.sessionInvalidated](credentialsession/errorcode/sessioninvalidated.md)
  The client requested invalidation of the session.
### Command error codes
- [CredentialSession.ErrorCode.commandNotSupported](credentialsession/errorcode/commandnotsupported.md)
  Your app attempted an unsupported Secure Element command.
### Network-related error codes
- [CredentialSession.ErrorCode.network](credentialsession/errorcode/network.md)
  The device’s internet connection is offline.
### Presentment intent assertion error codes
- [CredentialSession.ErrorCode.presentmentIntentAssertionTimeout](credentialsession/errorcode/presentmentintentassertiontimeout.md)
  The presentment intent assertion timed out.
### UIKit error codes
- [CredentialSession.ErrorCode.invalidView](credentialsession/errorcode/invalidview.md)
  The provided UIKit view is invalid.
### Hardware error codes
- [CredentialSession.ErrorCode.insufficientSpace](credentialsession/errorcode/insufficientspace.md)
  The hardware storage has insufficient space for the attempted provisioning.
### Temporary error codes
- [CredentialSession.ErrorCode.resourceUnavailable](credentialsession/errorcode/resourceunavailable.md)
  The requested resource is unavailable.
- [CredentialSession.ErrorCode.acquiredResourceRelinquished](credentialsession/errorcode/acquiredresourcerelinquished.md)
  The system relinquished an underlying shared resource, preventing the operation from completing.
### Miscellaneous error codes
- [CredentialSession.ErrorCode.invalidInput](credentialsession/errorcode/invalidinput.md)
  One or more parameters is invalid.
- [CredentialSession.ErrorCode.internalError](credentialsession/errorcode/internalerror.md)
  The framework encountered an internal error.
### Inspecting error causes
- [var failureReason: String?](credentialsession/errorcode/failurereason.md)
  A human-readable description of the error reason.
### Hashing
- [func hash(into: inout Hasher)](credentialsession/errorcode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](credentialsession/errorcode/hashvalue.md)
  The hash value.
### Comparing error codes
- [static func == (CredentialSession.ErrorCode, CredentialSession.ErrorCode) -> Bool](credentialsession/errorcode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](credentialsession/errorcode/equatable-implementations.md)
- [Error Implementations](credentialsession/errorcode/error-implementations.md)
- [LocalizedError Implementations](credentialsession/errorcode/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/errorcode)*