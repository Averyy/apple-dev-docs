# createCredentialRegistrationRequest(challenge:name:userID:)

**Framework**: Authentication Services  
**Kind**: method

Creates a registration request with a challenge, name, and user ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

#### Return Value

A public key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.
- `name`: The name of the user.
- `userID`: A user identifier.

## See Also

- [var relyingPartyIdentifier: String](asauthorizationplatformpublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialassertionrequest(challenge:).md)
  Creates an assertion request with a challenge.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:requeststyle:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:))*