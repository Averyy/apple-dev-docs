# key

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The key of the metadata item.

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
@NSCopying
var key: (any NSCopying & NSObjectProtocol)? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) id<NSCopying,NSObject> key;
```

#### Discussion

The key property contains the true key used to identify the contents of the metadata item. This value is specific to the key space of the metadata item.

## See Also

### Accessing keys and key spaces
- [var commonKey: AVMetadataKey?](./commonkey.md)
  The common key of the metadata item.
- [var keySpace: AVMetadataKeySpace?](./keyspace.md)
  The key space for the metadata item’s key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/key)*