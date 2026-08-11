# fetchDescriptor

**Framework**: SwiftData  
**Kind**: property

The fetch descriptor used to query the model context.

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
final var fetchDescriptor: FetchDescriptor<Element> { get }
```

#### Discussion

This descriptor defines the complete fetch criteria including predicate, sort descriptors, and other fetch options. It is configured at initialization and can be indirectly modified through the [`filterBy`](resultsobserver/filterby.md) and [`sortBy`](resultsobserver/sortby.md) computed properties.

## See Also

- [var filterBy: Predicate<Element>?](resultsobserver/filterby.md)
  The predicate used to filter which models are included in the results.
- [let modelContext: ModelContext](resultsobserver/modelcontext.md)
  The model context from which models are fetched.
- [var sortBy: [SortDescriptor<Element>]](resultsobserver/sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](resultsobserver/sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](resultsobserver/sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](resultsobserver/sectionby.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/fetchdescriptor)*