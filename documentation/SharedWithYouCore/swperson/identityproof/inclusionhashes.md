# inclusionHashes

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The hashes of missing Merkle tree nodes that can provide proof of inclusion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var inclusionHashes: [Data] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSData *> * inclusionHashes;
```

## Discussion

The data contains an array of SHA256 hash of the user’s combined public identities.

## See Also

### Accessing attributes
- [var publicKey: Data](./publickey.md)
  The public key of local device.
- [var publicKeyIndex: Int](./publickeyindex.md)
  The index of the local public key in the Merkle tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identityproof/inclusionhashes)*