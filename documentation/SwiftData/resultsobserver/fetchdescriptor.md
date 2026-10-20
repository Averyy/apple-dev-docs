# fetchDescriptor

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The fetch descriptor used to query the model context.

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
final var fetchDescriptor: FetchDescriptor<Element> { get }
```

#### Discussion

This descriptor defines the complete fetch criteria including predicate, sort descriptors, and other fetch options. It is configured at initialization and can be indirectly modified through the [`filterBy`](./filterby.md) and [`sortBy`](./sortby.md) computed properties.

## See Also

### Accessing observer properties
- [var filterBy: Predicate<Element>?](./filterby.md)
  The predicate used to filter which models are included in the results.
- [let modelContext: ModelContext](./modelcontext.md)
  The model context from which models are fetched.
- [var sortBy: [SortDescriptor<Element>]](./sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](./sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](./sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](./sectionby.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/fetchdescriptor)*