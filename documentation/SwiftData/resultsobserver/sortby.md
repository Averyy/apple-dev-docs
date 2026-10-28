# sortBy

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The sort descriptors used to order the results.

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
final var sortBy: [SortDescriptor<Element>] { get set }
```

## Discussion

Setting this property updates the underlying [`fetchDescriptor`](./fetchdescriptor.md)‘s sort descriptors and immediately refetches on the calling actor. When sectioning is active, the section’s sort descriptor is automatically re-prepended if not already the first descriptor. A `SortDescriptor` by `persistentModelID` is appended automatically if not already present to ensure stable ordering for difference computation.

## See Also

### Accessing observer properties
- [var fetchDescriptor: FetchDescriptor<Element>](./fetchdescriptor.md)
  The fetch descriptor used to query the model context.
- [var filterBy: Predicate<Element>?](./filterby.md)
  The predicate used to filter which models are included in the results.
- [let modelContext: ModelContext](./modelcontext.md)
  The model context from which models are fetched.
- [var sectionBy: PartialKeyPath<Element>?](./sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](./sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](./sectionby.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/sortby)*