# SectionedResults

**Framework**: SwiftData  
**Kind**: struct

A `RandomAccessCollection` of [`ResultsSection`](resultssection.md) instances representing sectioned query results.

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
struct SectionedResults<Element, SectionTitle> where Element : PersistentModel, SectionTitle : Hashable
```

#### Overview

`SectionedResults` is the result type for sectioned `@Query` properties. Iterating it yields sections; each section is itself a `RandomAccessCollection` of model elements. Use [`subscript(sectionTitle:)`](sectionedresults/subscript(sectiontitle:).md) for O(1) lookup by section title.

```swift
@Query(sort: \.name, sectionBy: \.category)
var items: SectionedResults<Item, String>

ForEach(items) { section in              // section: ResultsSection<Item, String>
    Section(section.title) {             // "Work", "Personal", …
        ForEach(section) { item in … }   // item: Item
    }
}

// O(1) named lookup
let workCount = items[sectionTitle: "Work"]?.count ?? 0
```

## Topics

### Instance Properties
- [var sectionTitles: [SectionTitle]](sectionedresults/sectiontitles.md)
  The section titles in order.
### Instance Methods
- [func contains(sectionTitle: SectionTitle) -> Bool](sectionedresults/contains(sectiontitle:).md)
  Returns whether a section with the given title exists in the collection.
- [func index(ofSectionTitled: SectionTitle) -> Int?](sectionedresults/index(ofsectiontitled:).md)
  Returns the ordered index of the section with the given title, or `nil` if not found.
### Subscripts
- [subscript(sectionTitle _: SectionTitle) -> ResultsSection<Element, SectionTitle>?](sectionedresults/subscript(sectiontitle:).md)
  Returns the section with the given title, or `nil` if no such section exists.
### Default Implementations
- [Equatable Implementations](sectionedresults/equatable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/sectionedresults)*