# createCredentialAssertionRequestWithClientData:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Creates a credential assertion request for authenticating to the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```objc
- (ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest *) createCredentialAssertionRequestWithClientData:(ASPublicKeyCredentialClientData *) clientData;
```

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.

## See Also

### Creating credential assertion requests
- [- createCredentialRegistrationRequestWithClientData:displayName:name:userID:](./createcredentialregistrationrequestwithclientdata_displayname_name_userid_.md)
  Creates a credential registration request for registering a new password with the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-4gzot/createcredentialassertionrequestwithclientdata:)*