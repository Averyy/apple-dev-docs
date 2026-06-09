# ResultsSection

**Framework**: SwiftData  
**Kind**: struct

A section of fetched results grouped by a common section key path value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ResultsSection<Element, SectionName> where Element : PersistentModel, SectionName : Hashable
```

#### Overview

Each section represents a group of elements that share the same value for the `sectionBy` key path used at creation.

You access sections through [`sections`](resultsobserver/sections.md) or `Query.sections`. Each section conforms to `RandomAccessCollection` — iterate it directly to access its elements, and use [`name`](resultssection/name.md) (or [`id`](resultssection/id.md)) to access the section identifier.

## Topics

### Accessing section properties
- [var id: SectionName](resultssection/id.md)
  The unique identifier for the section, which is its [`name`](resultssection/name.md).
- [let name: SectionName](resultssection/name.md)
  The identifier of the section.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Identifiable](../Swift/Identifiable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [subscript(sectionName _: SectionName) -> ResultsSection<Element, SectionName>?](resultssectioncollection/subscript(sectionname:).md)
  Returns the section with the given name, or `nil` if no such section exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssection)*