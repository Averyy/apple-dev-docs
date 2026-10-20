# ASAuthorizationAccountCreationProvider

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@objc
class ASAuthorizationAccountCreationProvider
```

## Topics

### Initializers
- [init()](./asauthorizationaccountcreationprovider/init%28%29.md)
### Instance Methods
- [func createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers: [ASContactIdentifierRequest], shouldRequestName: Bool, relyingPartyIdentifier: String, challenge: Data, userID: Data) -> ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest](./asauthorizationaccountcreationprovider/createplatformpublickeycredentialregistrationrequest%28acceptedcontactidentifiers,shouldrequestname,relyingpartyidentifier,challenge,userid%29.md)
  Create a new account creation request backed by a platform public key credential, i.e. a passkey.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](./asauthorizationprovider.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider)*