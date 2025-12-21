# createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers:shouldRequestName:relyingPartyIdentifier:challenge:userID:)

**Framework**: Authentication Services  
**Kind**: method

Create a new account creation request backed by a platform public key credential, i.e. a passkey.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers: [ASContactIdentifierRequest], shouldRequestName: Bool, relyingPartyIdentifier: String, challenge: Data, userID: Data) -> ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest
```

## Parameters

- `acceptedContactIdentifiers`: An ordered list of contact identifiers that the user can choose from during account creation. The order of this list indicates preference. Exactly one contact identifier from this list will be included in the response.
- `shouldRequestName`: Whether to request the user’s name.
- `relyingPartyIdentifier`: The Relying Party to register the passkey with, generally a domain name.
- `challenge`: A single-use challenge to be signed by the created passkey.
- `userID`: A stable, opaque identifier for the created account. This will be saved as the userID for the created passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider/createplatformpublickeycredentialregistrationrequest(acceptedcontactidentifiers:shouldrequestname:relyingpartyidentifier:challenge:userid:))*