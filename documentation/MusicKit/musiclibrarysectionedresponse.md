# MusicLibrarySectionedResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a library sectioned request.

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
struct MusicLibrarySectionedResponse<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

## Topics

### Instance Properties
- [let sections: [MusicLibrarySection<SectionType, MusicItemType>]](musiclibrarysectionedresponse/sections.md)
  An array of sections that match the filters on the originating library request.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiclibrarysectionedresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiclibrarysectionedresponse/customstringconvertible-implementations.md)
- [Equatable Implementations](musiclibrarysectionedresponse/equatable-implementations.md)
- [Hashable Implementations](musiclibrarysectionedresponse/hashable-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysectionedresponse)*