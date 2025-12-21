# Password use in web browsers

**Framework**: Authentication Services

Register and authenticate website users by using passwords.

#### Overview

If your browser app uses [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) to display web content, [`WebKit`](https://developer.apple.com/documentation/WebKit) automatically handles `WebAuthentication` challenges in webpages and requests credentials from the person using the browser. If your browser app uses an alternative web browser engine — for example, an alternate browser engine for iPhone that you write using [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit) — when the website makes a `WebAuthentication` challenge, use [`ASAuthorizationController`](asauthorizationcontroller.md) to discover and use credentials to respond to the challenge.  [`ASAuthorizationController`](asauthorizationcontroller.md) works with passwords the system stores on the keychain or that third-party credential managers control.

## Topics

### Website authorization
- [class ASAuthorizationWebBrowserPublicKeyCredentialManager](asauthorizationwebbrowserpublickeycredentialmanager.md)
  A class that you use to request access to a person’s passkeys in a web browser, and that reports on the access status.
### Website authentication requests
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialassertionrequest.md)
  An interface you use to respond to authentication challenges in a web browser.
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialregistrationrequest.md)
  An interface you use to respond to password-creation challenges in a web browser.
### Website credential providers
- [protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s.md)
  A protocol for creating passkey requests.

## See Also

- [Password AutoFill](../Security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class ASAuthorizationPasswordProvider](asauthorizationpasswordprovider.md)
  A mechanism for generating requests to perform keychain credential sharing.
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/password-use-in-web-browsers)*