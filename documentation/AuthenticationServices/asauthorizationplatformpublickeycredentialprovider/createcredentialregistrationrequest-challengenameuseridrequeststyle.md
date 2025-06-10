# createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)

**Framework**: Authentication Services  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func createCredentialRegistrationRequest(challenge: Data, name: String, userID: Data, requestStyle: ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle) -> ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest
```

## Parameters

- `challenge`: The challenge to sign.
- `name`: The user name for the new credential.
- `userID`: An identifier to be stored alongside the credential, which will be returned with the credential when it is used to authenticate.
- `requestStyle`: The style for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge:name:userid:requeststyle:))*