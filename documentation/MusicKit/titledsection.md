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

### Operators
- [static func == (TitledSection, TitledSection) -> Bool](titledsection/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](titledsection/hashvalue.md)
  The hash value.
- [var id: MusicItemID](titledsection/id-swift.property.md)
  The unique identifier for the titled section.
- [let title: String](titledsection/title.md)
  The title of the section.
### Instance Methods
- [func hash(into: inout Hasher)](titledsection/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [TitledSection.ID](titledsection/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](titledsection/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/titledsection)*