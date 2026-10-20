# CredentialSession.ErrorCode

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

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
- [CredentialSession.ErrorCode.userNotAuthorized](./errorcode/usernotauthorized.md)
  The person using the app isn’t authorized to perform the operation.
- [CredentialSession.ErrorCode.accessDenied](./errorcode/accessdenied.md)
  The person using the app declined to grant permission for the operation.
- [CredentialSession.ErrorCode.clientNotInForeground](./errorcode/clientnotinforeground.md)
  Your app isn’t in the foreground, which is required to use the credential session.
- [CredentialSession.ErrorCode.userCanceledAuthorization](./errorcode/usercanceledauthorization.md)
  The person using the app dismissed the authorization sheet.
- [CredentialSession.ErrorCode.userAuthorizationTimedOut](./errorcode/userauthorizationtimedout.md)
  Authorization timed out while waiting for the person using the app.
- [CredentialSession.ErrorCode.featureUnavailable](./errorcode/featureunavailable.md)
  The feature is unavailable.
- [CredentialSession.ErrorCode.ineligible](./errorcode/ineligible.md)
  The current device and user configuation are ineligible to use this service.
- [CredentialSession.ErrorCode.conditionsNotSatisfied](./errorcode/conditionsnotsatisfied.md)
  The iCloud account or passcode of the person using the app don’t satisfy the conditions to use this service.
### Credential error codes
- [CredentialSession.ErrorCode.invalidCredentialState](./errorcode/invalidcredentialstate.md)
  A credential is in a state that doesn’t permit that function.
- [CredentialSession.ErrorCode.credentialDoesNotExist](./errorcode/credentialdoesnotexist.md)
  The credential doesn’t exist, or you don’t have access to it.
- [CredentialSession.ErrorCode.instanceDoesNotExist](./errorcode/instancedoesnotexist.md)
  The instance doesn’t exist in the target credential.
### Session error codes
- [CredentialSession.ErrorCode.invalidSessionState](./errorcode/invalidsessionstate.md)
  The session is in a state that doesn’t permit that function.
- [CredentialSession.ErrorCode.sessionInvalidated](./errorcode/sessioninvalidated.md)
  The client requested invalidation of the session.
### Command error codes
- [CredentialSession.ErrorCode.commandNotSupported](./errorcode/commandnotsupported.md)
  Your app attempted an unsupported Secure Element command.
### Network-related error codes
- [CredentialSession.ErrorCode.network](./errorcode/network.md)
  The device’s internet connection is offline.
### Presentment intent assertion error codes
- [CredentialSession.ErrorCode.presentmentIntentAssertionTimeout](./errorcode/presentmentintentassertiontimeout.md)
  The presentment intent assertion timed out.
### UIKit error codes
- [CredentialSession.ErrorCode.invalidView](./errorcode/invalidview.md)
  The provided UIKit view is invalid.
### Hardware error codes
- [CredentialSession.ErrorCode.insufficientSpace](./errorcode/insufficientspace.md)
  The hardware storage has insufficient space for the attempted provisioning.
### Temporary error codes
- [CredentialSession.ErrorCode.resourceUnavailable](./errorcode/resourceunavailable.md)
  The requested resource is unavailable.
- [CredentialSession.ErrorCode.acquiredResourceRelinquished](./errorcode/acquiredresourcerelinquished.md)
  The system relinquished an underlying shared resource, preventing the operation from completing.
### Miscellaneous error codes
- [CredentialSession.ErrorCode.invalidInput](./errorcode/invalidinput.md)
  One or more parameters is invalid.
- [CredentialSession.ErrorCode.internalError](./errorcode/internalerror.md)
  The framework encountered an internal error.
### Enumeration Cases
- [CredentialSession.ErrorCode.invalidProductConfigID](./errorcode/invalidproductconfigid.md)
  The product configuration ID is invalid.
### Instance Properties
- [var failureReason: String?](./errorcode/failurereason.md)
  A string representation of the error code.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/errorcode)*