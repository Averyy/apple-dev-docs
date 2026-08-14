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

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysection)*