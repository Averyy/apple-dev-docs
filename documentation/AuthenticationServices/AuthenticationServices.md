# Authentication Services

**Framework**: Authentication Services  
**Kind**: module

Make it easy for users to log into apps and services.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

#### Overview

Use the Authentication Services framework to improve the experience of users when they enter credentials to establish their identity.

- Give users the ability to sign into your services with their Apple ID.
- Enable users to look up their stored passwords from within the sign-in flow of an app.
- Provide a passwordless registration and authentication workflow for apps and websites using iCloud Keychain or a physical security key.
- Perform automatic security upgrades from weak to strong passwords, or upgrade to using Sign in with Apple.
- Share data between an app and a web browser using technologies like OAuth to leverage existing web-based logins in the app.
- Create a single sign-on (SSO) experience in an enterprise app.

Simple and straightforward sign-up and sign-in flows reduce the burden on the user to remember passwords, which may improve security.

## Topics

### Authorization requests
- [class ASAuthorizationController](asauthorizationcontroller.md)
  A controller that manages authorization requests that a provider creates.
- [struct AuthorizationController](authorizationcontroller.md)
  A SwiftUI environment value that views use to perform authorization requests.
- [enum ASAuthorizationResult](asauthorizationresult.md)
  Describes the outcome of a successful authorization request.
### Sign In with Apple
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
- [class ASAuthorizationAppleIDCredential](asauthorizationappleidcredential.md)
  A credential that results from a successful Apple ID authentication.
### Passwords
- [Password AutoFill](../Security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASAuthorizationPasswordProvider](asauthorizationpasswordprovider.md)
  A mechanism for generating requests to perform keychain credential sharing.
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.
### Passkeys
- [Public-Private Key Authentication](public-private-key-authentication.md)
  Register and authenticate users with passkeys and security keys, without using passwords.
- [Passkey use in web browsers](passkey-use-in-web-browsers.md)
  Register and authenticate website users by using passkeys.
- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md)
  Allow users to sign in to a service without typing a password.
### Web authentication sessions
- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)
  Use a web authentication session to authenticate a user in your app.
- [Securing Logins with iCloud Keychain Verification Codes](securing-logins-with-icloud-keychain-verification-codes.md)
  Use time-based codes generated on-device for a secure authentication experience.
- [class ASWebAuthenticationSession](aswebauthenticationsession.md)
  A session that an app uses to authenticate a user through a web service.
- [struct WebAuthenticationSession](webauthenticationsession.md)
  A SwiftUI environment value that views use to authenticate someone using a web service.
- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)
  Extend your web browser app to handle web authentication requests from other apps.
- [class ASWebAuthenticationSessionWebBrowserSessionManager](aswebauthenticationsessionwebbrowsersessionmanager.md)
  A session manager that mediates sharing data between an app and a web browser.
- [ASWebAuthenticationSessionWebBrowserSupportCapabilities](../BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities.md)
  A collection of keys that a browser app uses to declare its ability to handle authentication requests from other apps.
### AutoFill credentials
- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)
  Help people efficiently perform multifactor authentication.
- [AutoFill Credential Provider Entitlement](../BundleResources/Entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md)
  A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
- [class ASCredentialProviderViewController](ascredentialproviderviewcontroller.md)
  A view controller that a password manager app uses to extend AutoFill.
### Credential migration
- [class ASCredentialExportManager](ascredentialexportmanager.md)
  A class to manage exporting credentials.
- [class ASCredentialImportManager](ascredentialimportmanager.md)
  A class to manage importing credentials.
### Single sign-on (SSO)
- [Enterprise single sign-on (SSO)](enterprise-single-sign-on-sso.md)
- [Platform single sign-on (SSO)](platform-single-sign-on-sso.md)
  Use credentials from macOS login to perform single sign-on with an identity provider.
### Apple TV authentication
- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [struct ASAuthorizationCustomMethod](asauthorizationcustommethod.md)
  The custom authorization method.
### Automatic security upgrades
- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationController](asaccountauthenticationmodificationcontroller.md)
  An object that performs a request to modify an account’s authentication properties.
- [class ASAccountAuthenticationModificationViewController](asaccountauthenticationmodificationviewcontroller.md)
  A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.
- [class ASAccountAuthenticationModificationExtensionContext](asaccountauthenticationmodificationextensioncontext.md)
  An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.
### Reference
- [AuthenticationServices Enumerations](authenticationservices-enumerations.md)
- [AuthenticationServices Data Types](authenticationservices-data-types.md)
### Classes
- [class ASAuthorizationProviderExtensionUserLoginConfiguration](asauthorizationproviderextensionuserloginconfiguration.md)
- [class ASOneTimeCodeCredentialIdentity](asonetimecodecredentialidentity.md)
### Protocols
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialassertionrequest.md)
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s.md)
  A protocol for creating passkey requests.
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialregistrationrequest.md)
### Structures
- [struct ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionencryptionalgorithm.md)
- [struct ASAuthorizationProviderExtensionSigningAlgorithm](asauthorizationproviderextensionsigningalgorithm.md)
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct.md)
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct.md)
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct.md)
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct.md)
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct.md)
  This type represents the inputs for the WebAuthentication PRF extension, when used during assertion requests. The PRF extension lets you create general purpose SymmetricKeys from passkeys, which could useful for tasks such as encryption of user data. The same input values used with the same passkey will always produce the same SymmetricKey.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionOutput](asauthorizationpublickeycredentialprfassertionoutput-swift.struct.md)
  The outputs of the WebAuthentication PRF extension, when requested during an assertion. This object represents one or two SymmetricKeys which are available anywhere the passkey can be used. These are general purpose keys which can be used for application-specific needs, such as encryption of user data. These keys should not be stored or exported. They should only ever be derived as the result of an assertion operation, and then discarded when finished.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct.md)
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct.md)
- [struct ASImportableEditableField](asimportableeditablefield.md)
  A field that someone can edit within a credential.
- [struct ASPasskeyAssertionCredentialExtensionInput](aspasskeyassertioncredentialextensioninput-swift.struct.md)
- [struct ASPasskeyAssertionCredentialExtensionOutput](aspasskeyassertioncredentialextensionoutput-swift.struct.md)
- [struct ASPasskeyRegistrationCredentialExtensionInput](aspasskeyregistrationcredentialextensioninput-swift.struct.md)
- [struct ASPasskeyRegistrationCredentialExtensionOutput](aspasskeyregistrationcredentialextensionoutput-swift.struct.md)
- [struct ASPublicKeyCredentialClientData](aspublickeycredentialclientdata-swift.struct.md)
### Variables
- [let ASCredentialExchangeActivity: String](ascredentialexchangeactivity.md)
  The activity type used in user activity objects sent to importing apps.
- [let ASCredentialImportToken: String](ascredentialimporttoken.md)
  The key for the token in the user info dictionary of the user activity sent to importing apps.
### Enumerations
- [enum ASPasskeyCredentialExtensionInput](aspasskeycredentialextensioninput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AuthenticationServices)*