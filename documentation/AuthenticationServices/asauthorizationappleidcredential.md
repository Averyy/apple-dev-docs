# ASAuthorizationAppleIDCredential

**Framework**: Authentication Services  
**Kind**: class

A credential that results from a successful Apple ID authentication.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class ASAuthorizationAppleIDCredential
```

## Topics

### Identifying a User
- [var identityToken: Data?](asauthorizationappleidcredential/identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to the app.
- [var authorizationCode: Data?](asauthorizationappleidcredential/authorizationcode.md)
  A token that the app uses to interact with the server.
- [var state: String?](asauthorizationappleidcredential/state.md)
  An arbitrary string that your app provides to the request that generates the credential.
- [var user: String](asauthorizationappleidcredential/user.md)
  An identifier for the authenticated user.
### Getting Contact Information
- [var authorizedScopes: [ASAuthorization.Scope]](asauthorizationappleidcredential/authorizedscopes.md)
  The contact information the user authorized your app to access.
- [var fullName: PersonNameComponents?](asauthorizationappleidcredential/fullname.md)
  The user’s full name from their Apple ID or a user-submitted value provided from the Sign in with Apple UI.
- [var email: String?](asauthorizationappleidcredential/email.md)
  The user’s email address.
### Detecting User Characteristics
- [var realUserStatus: ASUserDetectionStatus](asauthorizationappleidcredential/realuserstatus.md)
  A value that indicates whether the user appears to be a real person.
- [enum ASUserDetectionStatus](asuserdetectionstatus.md)
  Possible values for the real user indicator.
### Instance Properties
- [var userAgeRange: ASUserAgeRange](asauthorizationappleidcredential/useragerange.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing User Authentication with Sign in with Apple](implementing-user-authentication-with-sign-in-with-apple.md)
  Provide a way for users of your app to set up an account and start using your services.
- [Simplifying User Authentication in a tvOS App](simplifying-user-authentication-in-a-tvos-app.md)
  Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.
- [struct SignInWithAppleButton](signinwithapplebutton.md)
  The view that creates the Sign in with Apple button for display.
- [Sign in with Apple Entitlement](../BundleResources/Entitlements/com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.
- [class ASAuthorizationAppleIDProvider](asauthorizationappleidprovider.md)
  A mechanism for generating requests to authenticate users based on their Apple ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential)*