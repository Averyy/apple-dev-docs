# TitledSection

**Framework**: MusicKit  
**Kind**: struct

A section you can use to request items from the library grouped by title.

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
struct TitledSection
```

#### Overview

For example, when you perform a library sectioned request of albums, the library sectioned response will contain albums grouped by the first letter of their title, and the [`title`](titledsection/title.md) property of this section will be equal to that first letter.

## Topics

### Instance Properties
- [var id: MusicItemID](titledsection/id.md)
  The unique identifier for the titled section.
- [let title: String](titledsection/title.md)
  The title of the section.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/titledsection)*