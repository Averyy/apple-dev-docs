# ASAuthorizationAccountCreationProvider

**Framework**: Authentication Services  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@objc
class ASAuthorizationAccountCreationProvider
```

## Topics

### Initializers
- [init()](asauthorizationaccountcreationprovider/init.md)
### Instance Methods
- [func createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers: [ASContactIdentifierRequest], shouldRequestName: Bool, relyingPartyIdentifier: String, challenge: Data, userID: Data) -> ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest](asauthorizationaccountcreationprovider/createplatformpublickeycredentialregistrationrequest(acceptedcontactidentifiers:shouldrequestname:relyingpartyidentifier:challenge:userid:).md)
  Create a new account creation request backed by a platform public key credential, i.e. a passkey.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider)*