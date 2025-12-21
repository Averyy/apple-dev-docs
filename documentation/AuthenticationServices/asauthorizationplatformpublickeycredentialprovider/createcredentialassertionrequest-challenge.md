# createCredentialAssertionRequest(challenge:)

**Framework**: Authentication Services  
**Kind**: method

Creates an assertion request with a challenge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationPlatformPublicKeyCredentialAssertionRequest
```

#### Return Value

A public key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.

## See Also

- [var relyingPartyIdentifier: String](asauthorizationplatformpublickeycredentialprovider/relyingpartyidentifier.md)
  The domain name of the service to register or authorize against.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:).md)
  Creates a registration request with a challenge, name, and user ID.
- [func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:requeststyle:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialassertionrequest(challenge:))*