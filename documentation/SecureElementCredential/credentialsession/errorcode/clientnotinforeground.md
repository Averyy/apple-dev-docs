# CredentialSession.ErrorCode.clientNotInForeground

**Framework**: SecureElementCredential  
**Kind**: case

Your app isn’t in the foreground, which is required to use the credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case clientNotInForeground
```

## See Also

- [CredentialSession.ErrorCode.userNotAuthorized](credentialsession/errorcode/usernotauthorized.md)
  The person using the app isn’t authorized to perform the operation.
- [CredentialSession.ErrorCode.accessDenied](credentialsession/errorcode/accessdenied.md)
  The person using the app declined to grant permission for the operation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/errorcode/clientnotinforeground)*