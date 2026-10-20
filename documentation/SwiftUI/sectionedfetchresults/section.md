# SectionedFetchResults.Section

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A collection of fetched results that share a specified identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Section
```

#### Overview

Examine a `Section` instance to find the entities that satisfy a [`SectionedFetchRequest`](../sectionedfetchrequest.md) predicate, and that have a particular property with the value stored in the section’s [`id`](./section/id.md) parameter. You specify which property by setting the fetch request’s `sectionIdentifier` parameter during initialization, or by modifying the corresponding [`SectionedFetchResults`](../sectionedfetchresults.md) instance’s [`sectionIdentifier`](./sectionidentifier.md) property.

Obtain specific sections by treating the fetch results as a collection. For example, consider the following property declaration that fetches `Quake` managed objects that the [Loading and displaying a large data feed](../loading-and-displaying-a-large-data-feed.md) sample code project defines to store earthquake data:

```swift
@SectionedFetchRequest<String, Quake>(
    sectionIdentifier: \.day,
    sortDescriptors: [SortDescriptor(\.time, order: .reverse)]
)
private var quakes: SectionedFetchResults<String, Quake>
```

Get the first section using a subscript:

```swift
let firstSection = quakes[0]
```

Alternatively, you can loop over the sections to create a list of sections.

```swift
ForEach(quakes) { section in
    Text("Section \(section.id) has \(section.count) elements")
}
```

The sections also act as collections, which means you can use elements like the [`count`](../../Swift/collection/count.md) property in the example above.

## Topics

### Identifying the section
- [let id: SectionIdentifier](./section/id.md)
  The value that all entities in the section share for a specified key path.
### Getting indices
- [var startIndex: Int](./section/startindex.md)
  The index of the first entity in the section.
- [var endIndex: Int](./section/endindex.md)
  The index that’s one greater than that of the last entity in the section.
### Getting results
- [subscript(Int) -> Result](./section/subscript%28_%29.md)
  Gets the entity at the specified index within the section.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Identifiable](../../Swift/identifiable.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Configuring the associated sectioned fetch request
- [var nsPredicate: NSPredicate?](./nspredicate.md)
  The request’s predicate.
- [var sortDescriptors: [SortDescriptor<Result>]](./sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](./nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.
- [var sectionIdentifier: KeyPath<Result, SectionIdentifier>](./sectionidentifier.md)
  The key path that the system uses to group fetched results into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchresults/section)*