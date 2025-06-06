# ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest

**Framework**: Authentication Services  
**Kind**: protocol

An interface you use to respond to passkey-creation challenges in a web browser.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialRegistrationRequest
```

## Topics

### Information about the assertion
- [var clientData: ASPublicKeyCredentialClientData?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/clientdata-5dk66.md)
  The client data to supply to the relying party.
- [var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]?](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/excludedcredentials.md)
  A list of passkeys that the relying party doesn’t accept for resolving the challenge.
- [var shouldShowHybridTransport: Bool](asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest/shouldshowhybridtransport.md)
  Whether a remote authenticator that communicates with the operating system using Bluetooth can resolve the challenge.

## Relationships

### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md)

## See Also

- [protocol ASAuthorizationWebBrowserExternallyAuthenticatableRequest](asauthorizationwebbrowserexternallyauthenticatablerequest.md)
  An authorization request for which a web browser can retrieve credentials.
- [protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialassertionrequest.md)
  An interface you use to respond to authentication challenges in a web browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialregistrationrequest)*