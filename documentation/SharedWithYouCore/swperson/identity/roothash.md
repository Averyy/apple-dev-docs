# rootHash

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The root hash of the tree that represents the individual’s identity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var rootHash: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * rootHash;
```

## Mentions

- [Adding custom collaboration to your app](../../../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Discussion

The data contains a SHA256 hash of the user’s combined public identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identity/roothash)*