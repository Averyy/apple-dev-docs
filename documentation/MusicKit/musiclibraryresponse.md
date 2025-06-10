# MusicLibraryResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a library request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MusicLibraryResponse<MusicItemType> where MusicItemType : MusicItem
```

## Topics

### Instance Properties
- [let items: MusicItemCollection<MusicItemType>](musiclibraryresponse/items.md)
  A collection of items that match the filters on the originating library request.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiclibraryresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiclibraryresponse/customstringconvertible-implementations.md)
- [Equatable Implementations](musiclibraryresponse/equatable-implementations.md)
- [Hashable Implementations](musiclibraryresponse/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibraryresponse)*