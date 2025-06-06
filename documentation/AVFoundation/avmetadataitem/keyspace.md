# keySpace

**Framework**: AVFoundation  
**Kind**: property

The key space for the metadata item’s key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var keySpace: AVMetadataKeySpace? { get }
```

#### Discussion

The key space that this property value specifies is typically the default key space for the metadata container that stores the metadata item.

AVFoundation uses key spaces to group related sets of keys. For example, the framework defines different key spaces for common keys, iTunes keys, ID3 keys, and QuickTime keys. Key spaces aid in filtering arrays of metadata items.

## See Also

- [var key: (any NSCopying & NSObjectProtocol)?](avmetadataitem/key.md)
  The key of the metadata item.
- [var commonKey: AVMetadataKey?](avmetadataitem/commonkey.md)
  The common key of the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/keyspace)*