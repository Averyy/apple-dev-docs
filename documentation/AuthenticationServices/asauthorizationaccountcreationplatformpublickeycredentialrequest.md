# ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest

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
class ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest
```

## Topics

### Instance Properties
- [let acceptedContactIdentifiers: [ASContactIdentifierRequest]](asauthorizationaccountcreationplatformpublickeycredentialrequest/acceptedcontactidentifiers.md)
  An ordered list of contact identifiers that the user can choose from during account creation. The order of this list indicates preference. Exactly one contact identifier from this list will be included in the response.
- [let challenge: Data](asauthorizationaccountcreationplatformpublickeycredentialrequest/challenge.md)
  A single-use challenge to be signed by the created passkey.
- [let relyingPartyIdentifier: String](asauthorizationaccountcreationplatformpublickeycredentialrequest/relyingpartyidentifier.md)
  The Relying Party to register the passkey with, generally a domain name.
- [let shouldRequestName: Bool](asauthorizationaccountcreationplatformpublickeycredentialrequest/shouldrequestname.md)
  Whether to request the user’s name.
- [let userID: Data](asauthorizationaccountcreationplatformpublickeycredentialrequest/userid.md)
  A stable, opaque identifier for the created account. This will be saved as the userID for the created passkey.
### Instance Methods
- [func encode(with: NSCoder)](asauthorizationaccountcreationplatformpublickeycredentialrequest/encode(with:).md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](asauthorizationrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredentialrequest)*