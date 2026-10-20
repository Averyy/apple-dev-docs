# ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest

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
class ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest
```

## Topics

### Instance Properties
- [let acceptedContactIdentifiers: [ASContactIdentifierRequest]](./asauthorizationaccountcreationplatformpublickeycredentialrequest/acceptedcontactidentifiers.md)
  An ordered list of contact identifiers that the user can choose from during account creation. The order of this list indicates preference. Exactly one contact identifier from this list will be included in the response.
- [let challenge: Data](./asauthorizationaccountcreationplatformpublickeycredentialrequest/challenge.md)
  A single-use challenge to be signed by the created passkey.
- [let relyingPartyIdentifier: String](./asauthorizationaccountcreationplatformpublickeycredentialrequest/relyingpartyidentifier.md)
  The Relying Party to register the passkey with, generally a domain name.
- [let shouldRequestName: Bool](./asauthorizationaccountcreationplatformpublickeycredentialrequest/shouldrequestname.md)
  Whether to request the user’s name.
- [let userID: Data](./asauthorizationaccountcreationplatformpublickeycredentialrequest/userid.md)
  A stable, opaque identifier for the created account. This will be saved as the userID for the created passkey.
### Instance Methods
- [func encode(with: NSCoder)](./asauthorizationaccountcreationplatformpublickeycredentialrequest/encode%28with%29.md)

## Relationships

### Inherits From
- [ASAuthorizationRequest](./asauthorizationrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredentialrequest)*