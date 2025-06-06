# ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest

**Framework**: Authentication Services  
**Kind**: protocol

An interface you use to respond to authentication challenges in a web browser.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest
```

## Topics

### Information about the assertion
- [var clientData: ASPublicKeyCredentialClientData?](asauthorizationwebbrowserplatformpublickeycredentialassertionrequest/clientdata-655pi.md)
  The client data to supply to the relying party.
- [var shouldShowHybridTransport: Bool](asauthorizationwebbrowserplatformpublickeycredentialassertionrequest/shouldshowhybridtransport.md)
  Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.

## Relationships

### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md)

## See Also

- [protocol ASAuthorizationWebBrowserExternallyAuthenticatableRequest](asauthorizationwebbrowserexternallyauthenticatablerequest.md)
  An authorization request for which a web browser can retrieve credentials.
- [protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest.md)
  An interface you use to respond to passkey-creation challenges in a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialassertionrequest)*