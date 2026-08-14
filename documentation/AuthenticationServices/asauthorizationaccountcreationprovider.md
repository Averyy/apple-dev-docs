# ASAuthorizationAccountCreationProvider

**Framework**: Authentication Services  
**Kind**: class

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
- [init()](asauthorizationaccountcreationprovider/init.md)
### Instance Methods
- [func createPlatformPublicKeyCredentialRegistrationRequest(acceptedContactIdentifiers: [ASContactIdentifierRequest], shouldRequestName: Bool, relyingPartyIdentifier: String, challenge: Data, userID: Data) -> ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest](asauthorizationaccountcreationprovider/createplatformpublickeycredentialregistrationrequest(acceptedcontactidentifiers:shouldrequestname:relyingpartyidentifier:challenge:userid:).md)
  Create a new account creation request backed by a platform public key credential, i.e. a passkey.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationProvider](asauthorizationprovider.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider)*