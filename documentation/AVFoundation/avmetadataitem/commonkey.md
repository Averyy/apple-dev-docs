# commonKey

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The common key of the metadata item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var commonKey: AVMetadataKey? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) AVMetadataKey commonKey;
```

#### Discussion

This value contains the key that most closely corresponds to the [`key`](./key.md) property, but that belongs to the common key space. You can use this key to locate metadata items irrespective of the underlying media format.

If the value of the [`keySpace`](./keyspace.md) property is [`common`](../avmetadatakeyspace/common.md), this property value contains the same key as the [`key`](./key.md) property.

## See Also

### Accessing keys and key spaces
- [var key: (any NSCopying & NSObjectProtocol)?](./key.md)
  The key of the metadata item.
- [var keySpace: AVMetadataKeySpace?](./keyspace.md)
  The key space for the metadata item’s key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/commonkey)*