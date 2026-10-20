# keySpace

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The key space of the metadata item’s key.

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
var keySpace: AVMetadataKeySpace? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) AVMetadataKeySpace keySpace;
```

#### Discussion

The key space that this property value specifies is typically the default key space for the metadata container that stores the metadata item.

## See Also

### Accessing keys and key spaces
- [var key: (any NSCopying & NSObjectProtocol)?](./key.md)
  The key for a mutable metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/keyspace)*