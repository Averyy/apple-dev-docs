# SWPerson.Identity

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

The unique identity for a person.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class Identity
```

```objc
@interface SWPersonIdentity : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Overview

This object represents an opaque Merkle tree where the root hash of the tree can uniquely identify the individual using the hash value of all of their devices. The individual’s devices use [`SWPerson.IdentityProof`](./identityproof.md) to prove themselves to be part of this identity, and can then be used for cryptographic signatures for that individual.

## Topics

### Creating a hash
- [init(rootHash: Data)](./identity/init%28roothash%29.md)
  Creates and initializes the hash.
### Accessing the hash
- [var rootHash: Data](./identity/roothash.md)
  The root hash of the tree that represents the individual’s identity.
### Initializers
- [init?(coder: NSCoder)](./identity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Accessing attributes
- [SWPerson.IdentityProof](./identityproof.md)
  An object that represents proof of inclusion to a Merkle tree.
- [SWPerson.SignedIdentityProof](./signedidentityproof.md)
  The signature that the system creates by signing the data with this person’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identity)*