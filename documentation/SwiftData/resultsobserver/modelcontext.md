# modelContext

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The model context from which models are fetched.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final let modelContext: ModelContext
```

## Discussion

This context is set at initialization and determines the data store and change-tracking scope for the observer.

## See Also

### Accessing observer properties
- [var fetchDescriptor: FetchDescriptor<Element>](./fetchdescriptor.md)
  The fetch descriptor used to query the model context.
- [var filterBy: Predicate<Element>?](./filterby.md)
  The predicate used to filter which models are included in the results.
- [var sortBy: [SortDescriptor<Element>]](./sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](./sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](./sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](./sectionby.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/modelcontext)*