# createCredentialAssertionRequest(clientData:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Create a credential assertion request, for authenticating to the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest
```

## Return Value

The credential assertion request, that you pass to [`ASAuthorizationController`](../asauthorizationcontroller.md).

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.

## See Also

### Creating requests
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28clientdata,name,userid%29.md)
  Create a credential registration request, for registering a new passkey with the relying party.
- [func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./createcredentialregistrationrequest%28clientdata,name,userid,requeststyle%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialassertionrequest(clientdata:))*