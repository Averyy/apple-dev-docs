# ASAuthorizationAppleIDProvider

**Framework**: Authentication Services  
**Kind**: class

A mechanism for generating requests to authenticate users based on their Apple ID.

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
class ASAuthorizationAppleIDProvider
```

#### Overview

You use a provider to create a request ([`ASAuthorizationAppleIDRequest`](asauthorizationappleidrequest.md)), which you then use to initialize a controller ([`ASAuthorizationController`](asauthorizationcontroller.md)) that performs the request:

```swift
let provider = ASAuthorizationAppleIDProvider()
let request = provider.createRequest()
let controller = ASAuthorizationController(authorizationRequests: [request])
```

On success, the controller’s delegate receives an authorization ([`ASAuthorization`](asauthorization.md)) containing a credential ([`ASAuthorizationAppleIDCredential`](asauthorizationappleidcredential.md)) that has an opaque [`user`](asauthorizationappleidcredential/user.md) identifier. You can use that identifier to later check the user’s credential state—for example, to see if authorization has been revoked—by calling the [`getCredentialState(forUserID:completion:)`](asauthorizationappleidprovider/getcredentialstate(foruserid:completion:).md) method:

```swift
let user = authorization.credential.user
provider.getCredentialState(forUserID: user) { state, error in
    // Check for error and examine the state.
}
```

## Topics

### Offering Sign In with Apple
- [class ASAuthorizationAppleIDButton](asauthorizationappleidbutton.md)
  A control you add to your interface that enables users to initiate the Sign In with Apple flow.
- [class WKInterfaceAuthorizationAppleIDButton](../WatchKit/WKInterfaceAuthorizationAppleIDButton.md)
  A button that you can use to trigger a Sign in with Apple request.
### Creating Requests
- [func createRequest() -> ASAuthorizationAppleIDRequest](asauthorizationappleidprovider/createrequest.md)
  Creates a new Apple ID authorization request.
- [class ASAuthorizationAppleIDRequest](asauthorizationappleidrequest.md)
  An OpenID authorization request that relies on the user’s Apple ID.
- [class ASAuthorizationOpenIDRequest](asauthorizationopenidrequest.md)
  An OpenID authorization request.
### Getting State
- [func getCredentialState(forUserID: String, completion: (ASAuthorizationAppleIDProvider.CredentialState, (any Error)?) -> Void)](asauthorizationappleidprovider/getcredentialstate(foruserid:completion:).md)
  Returns the credential state for the given user in a completion handler.
- [ASAuthorizationAppleIDProvider.CredentialState](asauthorizationappleidprovider/credentialstate.md)
  Possible values for the credential state of a user.
- [class let credentialRevokedNotification: NSNotification.Name](asauthorizationappleidprovider/credentialrevokednotification.md)
  A notification that indicates the user’s credentials have been revoked and they should be signed out.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing User Authentication with Sign in with Apple](implementing-user-authentication-with-sign-in-with-apple.md)
  Provide a way for users of your app to set up an account and start using your services.
- [Simplifying User Authentication in a tvOS App](simplifying-user-authentication-in-a-tvos-app.md)
  Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.
- [struct SignInWithAppleButton](signinwithapplebutton.md)
  The view that creates the Sign in with Apple button for display.
- [Sign in with Apple Entitlement](../BundleResources/Entitlements/com.apple.developer.applesignin.md)
  An entitlement that lets your app use Sign in with Apple.
- [class ASAuthorizationAppleIDCredential](asauthorizationappleidcredential.md)
  A credential that results from a successful Apple ID authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider)*