# MusicLibrarySection

**Framework**: MusicKit  
**Kind**: struct

A section for a library sectioned response.

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
@dynamicMemberLookup
struct MusicLibrarySection<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

#### Overview

Your app can access any property of the requested section type directly on this library section object.

Your app can also access the items contained in a library section with the [`items`](musiclibrarysection/items.md) property.

## Topics

### Instance Properties
- [let items: MusicItemCollection<MusicItemType>](musiclibrarysection/items.md)
  A collection of items that correspond to the children of the section.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<SectionType, T>) -> T](musiclibrarysection/subscript(dynamicmember:).md)
  A subscript that allows your app to access any property of the requested section type directly on this library section object.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiclibrarysection/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiclibrarysection/customstringconvertible-implementations.md)
- [Equatable Implementations](musiclibrarysection/equatable-implementations.md)
- [Hashable Implementations](musiclibrarysection/hashable-implementations.md)
- [Identifiable Implementations](musiclibrarysection/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysection)*