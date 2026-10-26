# createCredentialRegistrationRequestWithClientData:displayName:name:userID:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Creates a credential registration request for registering a new password with the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```objc
- (ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest *) createCredentialRegistrationRequestWithClientData:(ASPublicKeyCredentialClientData *) clientData displayName:(NSString *) displayName name:(NSString *) name userID:(NSData *) userID;
```

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.
- `displayName`: The proper name of the user.
- `name`: The person’s user name for their account with the relying party.
- `userID`: A unique identifier for the person’s account with the relying party.

## See Also

### Creating credential assertion requests
- [- createCredentialAssertionRequestWithClientData:](./createcredentialassertionrequestwithclientdata_.md)
  Creates a credential assertion request for authenticating to the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-4gzot/createcredentialregistrationrequestwithclientdata:displayname:name:userid:)*