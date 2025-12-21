# createCredentialRegistrationRequest(clientData:displayName:name:userID:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Creates a credential registration request for registering a new password with the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest
```

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.
- `displayName`: The proper name of the user.
- `name`: The person’s user name for their account with the relying party.
- `userID`: A unique identifier for the person’s account with the relying party.

## See Also

- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s/createcredentialassertionrequest(clientdata:).md)
  Creates a credential assertion request for authenticating to the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s/createcredentialregistrationrequest(clientdata:displayname:name:userid:))*