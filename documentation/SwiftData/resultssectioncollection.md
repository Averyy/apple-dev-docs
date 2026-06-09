# ResultsSectionCollection

**Framework**: SwiftData  
**Kind**: struct

A collection of sections as returned by [`sections`](resultsobserver/sections.md) or `Query.sections`.

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
struct ResultsSectionCollection<Element, SectionName> where Element : PersistentModel, SectionName : Hashable
```

#### Overview

This is a lightweight `RandomAccessCollection` of [`ResultsSection`](resultssection.md) instances, ordered by their first appearance in the sorted results.

Because each section’s [`name`](resultssection/name.md) is its identity, the collection provides O(1) lookup by section name via [`subscript(sectionName:)`](resultssectioncollection/subscript(sectionname:).md) and [`contains(sectionName:)`](resultssectioncollection/contains(sectionname:).md).

You typically access this collection through [`sections`](resultsobserver/sections.md) or `Query.sections`.

## Topics

### Finding sections
- [var sectionNames: [SectionName]](resultssectioncollection/sectionnames.md)
  The section names in order.
- [func contains(sectionName: SectionName) -> Bool](resultssectioncollection/contains(sectionname:).md)
  Returns whether a section with the given name exists in the collection.
- [func index(ofSectionNamed: SectionName) -> Int?](resultssectioncollection/index(ofsectionnamed:).md)
  Returns the ordered index of the section with the given name, or `nil` if not found.
### Retrieving sections
- [subscript(sectionName _: SectionName) -> ResultsSection<Element, SectionName>?](resultssectioncollection/subscript(sectionname:).md)
  Returns the section with the given name, or `nil` if no such section exists.
- [struct ResultsSection](resultssection.md)
  A section of fetched results grouped by a common section key path value.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var sections: ResultsSectionCollection<Element, String>](query/sections.md)
  The sections computed from the current results, grouped by the `sectionBy` key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssectioncollection)*