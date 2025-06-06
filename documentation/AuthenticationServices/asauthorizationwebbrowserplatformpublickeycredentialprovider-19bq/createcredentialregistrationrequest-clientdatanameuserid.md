# createCredentialRegistrationRequest(clientData:name:userID:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Create a credential registration request, for registering a new passkey with the relying party.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.6+
- macOS 13.5+

## Declaration

```swift
func createCredentialRegistrationRequest(clientData: ASPublicKeyCredentialClientData, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

#### Return Value

The credential registration request, that you pass to [`ASAuthorizationController`](asauthorizationcontroller.md).

## Parameters

- `clientData`: The client data that contains the reply to the relying party’s challenge.
- `name`: The person’s user name for their account with the relying party.
- `userID`: A unique identifier for the person’s account with the relying party.

## See Also

- [func createCredentialAssertionRequest(clientData: ASPublicKeyCredentialClientData) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialassertionrequest(clientdata:).md)
  Create a credential assertion request, for authenticating to the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredentialprovider-19bq/createcredentialregistrationrequest(clientdata:name:userid:))*