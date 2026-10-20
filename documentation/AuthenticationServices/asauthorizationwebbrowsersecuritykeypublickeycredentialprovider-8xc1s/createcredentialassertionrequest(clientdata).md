# createCredentialAssertionRequest(clientData:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a credential assertion request for authenticating to the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest
```

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.

## See Also

### Creating credential assertion requests
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28clientdata,displayname,name,userid%29.md)
  Creates a credential registration request for registering a new password with the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowsersecuritykeypublickeycredentialprovider-8xc1s/createcredentialassertionrequest(clientdata:))*