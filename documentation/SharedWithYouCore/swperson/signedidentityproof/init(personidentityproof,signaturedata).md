# init(personIdentityProof:signatureData:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and intializes a signed identity object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(personIdentityProof: SWPerson.IdentityProof, signatureData data: Data)
```

```objc
- (instancetype) initWithPersonIdentityProof:(SWPersonIdentityProof *) personIdentityProof signatureData:(NSData *) data;
```

## Parameters

- `personIdentityProof`: The [`SWPerson.IdentityProof`](../identityproof.md) the system uses to create the signed identity.
- `data`: The data for the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/signedidentityproof/init(personidentityproof:signaturedata:))*