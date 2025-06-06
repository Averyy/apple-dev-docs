# Supporting Security Key Authentication Using Physical Keys

**Framework**: Authenticationservices

Allow users to authenticate using NFC, USB, and Lightning security keys in your app or service.

#### Overview

Security key authentication supports physical security devices for authentication to web services, eliminating the need for passwords. Such devices are especially useful in high-security contexts with apps and websites that are able to handle the complexity that comes with account recovery due to security key loss.

Take special care when using physical devices for authentication. If the user loses the device or someone steals it, there is no way to perform authentication with associated services. Have a backup strategy in place for such events.

> ❗ **Important**:  You must have an associated domain with the `webcredentials` service type when making a registration or assertion request; otherwise, the request returns an error. See [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains) for more information.__

##### Register a New Account on a Service

The following code sets up the process of registration. Create an instance of [`ASAuthorizationSecurityKeyPublicKeyCredentialProvider`](asauthorizationsecuritykeypublickeycredentialprovider.md) and pass it your relying party identifier, which is usually the service’s domain name.

```swift
var challenge : NSData? // Obtain this from the server.
let securityKeyProvider = ASAuthorizationSecurityKeyPublicKeyCredentialProvider("example.com")
let securityKeyRequest = securityKeyProvider.createCredentialRegistrationRequest(challenge: challenge, displayName: "Anne Johnson", name: "annejohnson1@icloud.com", userID: "anne_johnson")
securityKeyRequest.credentialParameters = [ ASAuthorizationPublicKeyCredentialParameters(algorithm: ASCOSEAlgorithmIdentifier.ES256) ]
let authController = ASAuthorizationController([securityKeyRequest])
authController.delegate = self
authController.presentationContextProvider = self
authController.performRequests()

```

You’re responsible for communicating with the server to obtain the challenge. Create a security key request by calling [`createCredentialRegistrationRequest(challenge:displayName:name:userID:)`](asauthorizationsecuritykeypublickeycredentialprovider/createcredentialregistrationrequest(challenge:displayname:name:userid:).md) and passing in the list of parameters.

Then specify the parameters for the types of credentials that your server supports. Obtain an authorization controller by passing in an array that contains the security key request, and set the delegate and presentation context provider of the controller to a class that adopts [`ASAuthorizationControllerDelegate`](asauthorizationcontrollerdelegate.md). Finally, direct the controller to perform the request.

Because this is a registration request, the device displays a sheet asking the user to create a new credential.

##### Connect to a Service with an Existing Account

After the user establishes an account with a service, they can connect and authenticate using the physical security device.

Obtain the challenge from the server, then create an instance of [`ASAuthorizationSecurityKeyPublicKeyCredentialProvider`](asauthorizationsecuritykeypublickeycredentialprovider.md) and set its provider to the service URL. Set the challenge, and then create an [`ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest`](asauthorizationsecuritykeypublickeycredentialassertionrequest.md).

Create the authorization controller with the platform key request, set the controller’s delegate and presentation context provider, and direct the authorization controller to perform the request.

```swift
let securityKeyProvider = ASAuthorizationSecurityKeyPublicKeyCredentialProvider("example.com")
var challenge : NSData?
let securityKeyRequest = securityKeyProvider.createCredentialAssertionRequestWithChallenge(challenge)
let authController = ASAuthorizationController([securityKeyRequest])
authController.delegate = self
authController.presentationContextProvider = self
authController.performRequests()

```

The device displays a sheet instructing the user about how to use the physical security device.

> **Note**:  Unlike platform public key requests and other types of authorization requests, a security key request always shows a sign-in user interface. Ensure that your user is expecting to sign in with a security key before making a security key request.

##### Respond to the Request

[`ASAuthorizationControllerDelegate`](asauthorizationcontrollerdelegate.md) provides information about the outcome of a registration or authentication request. Adopt this protocol to determine how to react to authorization success or errors. The following code defines [`authorizationController(controller:didCompleteWithAuthorization:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:).md) to handle registration and assertion, as well as [`authorizationController(controller:didCompleteWithError:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md) to handle any errors:

```swift
func authorizationController(controller: controller, didCompleteWithAuthorization: authorization) {
  if let credential = authorization.credential as? ASAuthorizationSecurityKeyPublicKeyCredentialRegistration {
    // Take steps to handle the registration.
 } else if let credential = authorization.credential as? ASAuthorizationSecurityKeyPublicKeyCredentialAssertion {
    // Take steps to verify the challenge.
  } else {
    // Handle other authentication cases, such as Sign in with Apple.
}

func authorizationController(controller: controller, didCompleteWithError: error) {
  // Handle the error.
} 
```

If the authorization succeeds, obtain the credential from the authoriziation controller and determine whether it’s an [`ASAuthorizationSecurityKeyPublicKeyCredentialRegistration`](asauthorizationsecuritykeypublickeycredentialregistration.md) or an ` ```ASAuthorizationSecurityKeyPublicKeyCredentialAssertion``, and take appropriate steps. If your app uses other authorization cases, such as Sign in with Apple, handle those in this delegate method, as well.

If an error occurs during the authorization, the framework calls [`authorizationController(controller:didCompleteWithError:)`](asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:).md) and provides the specific error.

## See Also

- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md)
  Allow users to sign in to a service without typing a password.
- [Supporting passkeys](supporting-passkeys.md)
  Eliminate passwords for your users when they sign in to apps and websites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AuthenticationServices/supporting-security-key-authentication-using-physical-keys)*