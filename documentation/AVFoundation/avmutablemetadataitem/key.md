# key

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The key for a mutable metadata item.

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
var key: (any NSCopying & NSObjectProtocol)? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) id<NSCopying,NSObject> key;
```

## See Also

### Accessing keys and key spaces
- [var keySpace: AVMetadataKeySpace?](./keyspace.md)
  The key space of the metadata item’s key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/key)*