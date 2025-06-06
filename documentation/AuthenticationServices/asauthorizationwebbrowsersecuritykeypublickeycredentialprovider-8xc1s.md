# ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: protocol

A protocol for creating passkey requests.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider
```

## Topics

### Creating passkey assertion requests
- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s/createcredentialassertionrequest(clientdata:).md)
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s/createcredentialregistrationrequest(clientdata:displayname:name:userid:).md)

## Relationships

### Conforming Types
- [ASAuthorizationSecurityKeyPublicKeyCredentialProvider](asauthorizationsecuritykeypublickeycredentialprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s)*