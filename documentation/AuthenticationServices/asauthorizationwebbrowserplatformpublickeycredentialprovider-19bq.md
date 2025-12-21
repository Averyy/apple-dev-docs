# ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: protocol

A mechanism you use to provide public key credential requests to a browser app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
protocol ASAuthorizationWebBrowserPlatformPublicKeyCredentialProvider
```

## Topics

### Creating requests
- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialassertionrequest(clientdata:).md)
  Create a credential assertion request, for authenticating to the relying party.
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:).md)
  Create a credential registration request, for registering a new passkey with the relying party.
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:requeststyle:).md)

## Relationships

### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialProvider](asauthorizationplatformpublickeycredentialprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq)*