# SWPerson

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that tracks participants in a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWPerson
```

```objc
@interface SWPerson : NSObject
```

## Topics

### Creating participants
- [init(handle: String?, identity: SWPerson.Identity?, displayName: String, thumbnailImageData: Data?)](./swperson/init%28handle,identity,displayname,thumbnailimagedata%29.md)
  Creates and initializes a person object.
### Accessing attributes
- [SWPerson.Identity](./swperson/identity.md)
  The unique identity for a person.
- [SWPerson.IdentityProof](./swperson/identityproof.md)
  An object that represents proof of inclusion to a Merkle tree.
- [SWPerson.SignedIdentityProof](./swperson/signedidentityproof.md)
  The signature that the system creates by signing the data with this person’s identity.
### Initializers
- [init?(coder: NSCoder)](./swperson/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Manage collaboration participants
- [struct SWCollaborationIdentifier](./swcollaborationidentifier.md)
  A unique identifier for a collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson)*