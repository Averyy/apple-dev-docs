# key

**Framework**: AVFoundation  
**Kind**: property

The key of the metadata item.

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
@NSCopying
var key: (any NSCopying & NSObjectProtocol)? { get }
```

#### Discussion

The key property contains the true key used to identify the contents of the metadata item. This value is specific to the key space of the metadata item.

## See Also

- [var commonKey: AVMetadataKey?](avmetadataitem/commonkey.md)
  The common key of the metadata item.
- [var keySpace: AVMetadataKeySpace?](avmetadataitem/keyspace.md)
  The key space for the metadata item’s key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/key)*