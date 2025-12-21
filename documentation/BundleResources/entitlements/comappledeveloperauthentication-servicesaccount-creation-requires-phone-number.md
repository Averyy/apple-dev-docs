# Account Creation Requires Phone Number

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app requires someone to provide a phone number to create an account.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

#### Discussion

When your app calls [`createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers:shouldRequestName:relyingPartyIdentifier:challenge:userID:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAccountCreationProvider/createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers:shouldRequestName:relyingPartyIdentifier:challenge:userID:)) to start the account-creation flow, the `acceptedContactIdentifiers` array can contain [`ASContactIdentifierRequest.email`](https://developer.apple.com/documentation/AuthenticationServices/ASContactIdentifierRequest/email), [`ASContactIdentifierRequest.phoneNumber`](https://developer.apple.com/documentation/AuthenticationServices/ASContactIdentifierRequest/phoneNumber), or both. If the array only contains `phoneNumber`, then you must include the  `com.apple.developer.authentication-services.account-creation-requires-phone-number` entitlement in your app in Xcode, which states your app always requires a person’s phone number to create an account, with or without the use of the Account Creation API.

If your call to [`createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers:shouldRequestName:relyingPartyIdentifier:challenge:userID:)`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAccountCreationProvider/createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers:shouldRequestName:relyingPartyIdentifier:challenge:userID:)) allows use of an email to create an account, or a choice of email or phone number, you don’t need this entitlement.

## See Also

- [AutoFill Credential Provider Entitlement](entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md)
  A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
- [Sign in with Apple Entitlement](entitlements/com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.authentication-services.account-creation-requires-phone-number)*