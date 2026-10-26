# publicKeyIndex

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The index of the local public key in the Merkle tree.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var publicKeyIndex: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger publicKeyIndex;
```

#### Discussion

This data can be used to determine if the node is the left or the right child in the tree.

## See Also

### Accessing attributes
- [var inclusionHashes: [Data]](./inclusionhashes.md)
  The hashes of missing Merkle tree nodes that can provide proof of inclusion.
- [var publicKey: Data](./publickey.md)
  The public key of local device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identityproof/publickeyindex)*