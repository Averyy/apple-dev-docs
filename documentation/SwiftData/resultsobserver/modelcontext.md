# modelContext

**Framework**: SwiftData  
**Kind**: property

The model context from which models are fetched.

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
final let modelContext: ModelContext
```

#### Discussion

This context is set at initialization and determines the data store and change-tracking scope for the observer.

## See Also

- [var fetchDescriptor: FetchDescriptor<Element>](resultsobserver/fetchdescriptor.md)
  The fetch descriptor used to query the model context.
- [var filterBy: Predicate<Element>?](resultsobserver/filterby.md)
  The predicate used to filter which models are included in the results.
- [var sortBy: [SortDescriptor<Element>]](resultsobserver/sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](resultsobserver/sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: ResultsSectionCollection<Element, SectionName>?](resultsobserver/sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](resultsobserver/sectionby.md).
- [struct ResultsSectionCollection](resultssectioncollection.md)
  A collection of sections as returned by [`sections`](resultsobserver/sections.md) or `Query.sections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/modelcontext)*