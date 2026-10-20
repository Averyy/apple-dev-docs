# createCredentialRegistrationRequest(clientData:name:userID:requestStyle:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 16.6+
- macOS 15.0+

## Declaration

```swift
func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

## See Also

### Creating requests
- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28clientdata%29.md)
  Create a credential assertion request, for authenticating to the relying party.
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28clientdata,name,userid%29.md)
  Create a credential registration request, for registering a new passkey with the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:requeststyle:))*