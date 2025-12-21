# createCredentialRegistrationRequest(clientData:name:userID:requestStyle:)

**Framework**: Authentication Services  
**Kind**: method  
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

- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialassertionrequest(clientdata:).md)
  Create a credential assertion request, for authenticating to the relying party.
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:).md)
  Create a credential registration request, for registering a new passkey with the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:requeststyle:))*