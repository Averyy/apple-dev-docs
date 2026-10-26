# ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

A protocol for creating security key requests.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```objc
@protocol ASAuthorizationWebBrowserSecurityKeyPublicKeyCredentialProvider
```

## Topics

### Creating credential assertion requests
- [- createCredentialAssertionRequestWithClientData:](./asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-4gzot/createcredentialassertionrequestwithclientdata_.md)
  Creates a credential assertion request for authenticating to the relying party.
- [- createCredentialRegistrationRequestWithClientData:displayName:name:userID:](./asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-4gzot/createcredentialregistrationrequestwithclientdata_displayname_name_userid_.md)
  Creates a credential registration request for registering a new password with the relying party.

## Relationships

### Conforming Types
- [ASAuthorizationSecurityKeyPublicKeyCredentialProvider](./asauthorizationsecuritykeypublickeycredentialprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-4gzot)*