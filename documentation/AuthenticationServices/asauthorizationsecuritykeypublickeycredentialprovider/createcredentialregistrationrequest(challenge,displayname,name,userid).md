# createCredentialRegistrationRequest(challenge:displayName:name:userID:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Creates a registration request with a challenge, display name, and user ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func createCredentialRegistrationRequest(challenge: Data, displayName: String, name: String, userID: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest
```

```objc
- (ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest *) createCredentialRegistrationRequestWithChallenge:(NSData *) challenge displayName:(NSString *) displayName name:(NSString *) name userID:(NSData *) userID;
```

## Mentions

- [Supporting passkeys](../supporting-passkeys.md)
- [Supporting Security Key Authentication Using Physical Keys](../supporting-security-key-authentication-using-physical-keys.md)

## Return Value

A security key credential registration request.

## Parameters

- `challenge`: A stream of bytes that the server provides to prove an authenticator is valid.
- `displayName`: The proper name of the user.
- `name`: The name of the user.
- `userID`: The user’s account identifier.

## See Also

### Creating the request
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the service to authorize against.
- [func createCredentialAssertionRequest(challenge: Data) -> ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](./createcredentialassertionrequest%28challenge%29.md)
  Creates an assertion request with a challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialprovider/createcredentialregistrationrequest(challenge:displayname:name:userid:))*