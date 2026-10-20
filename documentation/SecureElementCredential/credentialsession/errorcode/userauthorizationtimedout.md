# CredentialSession.ErrorCode.userAuthorizationTimedOut

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

Authorization timed out while waiting for the person using the app.

**Availability**:
- iOS 18.1+ - Deprecated in 27.0
- iPadOS 18.1+ - Deprecated in 27.0

> **Deprecated**: This error is no longer thrown by the framework.

## Declaration

```swift
case userAuthorizationTimedOut
```

## See Also

### Authorization and permission error codes
- [CredentialSession.ErrorCode.userNotAuthorized](./usernotauthorized.md)
  The person using the app isn’t authorized to perform the operation.
- [CredentialSession.ErrorCode.accessDenied](./accessdenied.md)
  The person using the app declined to grant permission for the operation.
- [CredentialSession.ErrorCode.clientNotInForeground](./clientnotinforeground.md)
  Your app isn’t in the foreground, which is required to use the credential session.
- [CredentialSession.ErrorCode.userCanceledAuthorization](./usercanceledauthorization.md)
  The person using the app dismissed the authorization sheet.
- [CredentialSession.ErrorCode.featureUnavailable](./featureunavailable.md)
  The feature is unavailable.
- [CredentialSession.ErrorCode.ineligible](./ineligible.md)
  The current device and user configuation are ineligible to use this service.
- [CredentialSession.ErrorCode.conditionsNotSatisfied](./conditionsnotsatisfied.md)
  The iCloud account or passcode of the person using the app don’t satisfy the conditions to use this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/errorcode/userauthorizationtimedout)*