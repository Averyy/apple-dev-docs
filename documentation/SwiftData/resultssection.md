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
struct ResultsSection<Element, SectionTitle> where Element : PersistentModel, SectionTitle : Hashable
```

#### Overview

Each section represents a group of elements that share the same value for the `sectionBy` key path used at creation.

You access sections by iterating a [`SectionedResults`](sectionedresults.md) value returned by a sectioned `@Query`. Each section conforms to `RandomAccessCollection` — iterate it directly to access its elements, and use [`title`](resultssection/title.md) (or [`id`](resultssection/id.md)) to access the section grouping value.

```swift
@Query(sort: \.name, sectionBy: \.category)
var items: SectionedResults<Item, String>

ForEach(items) { section in
    Section(section.title) {          // "Work", "Personal", …
        ForEach(section) { item in … } // Item elements
    }
}
```

## Topics

### Accessing section properties
- [var id: SectionTitle](resultssection/id.md)
  The unique identifier for the section, which is its [`title`](resultssection/title.md).
### Instance Properties
- [let title: SectionTitle](resultssection/title.md)
  The identifier of the section.
### Default Implementations
- [Equatable Implementations](resultssection/equatable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssection)*