# filterBy

**Framework**: SwiftData  
**Kind**: property

The predicate used to filter which models are included in the results.

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
final var filterBy: Predicate<Element>? { get set }
```

#### Discussion

Setting this property updates the underlying [`fetchDescriptor`](resultsobserver/fetchdescriptor.md)’s predicate and immediately refetches on the calling actor — results are synchronously up to date before the setter returns. Set to `nil` to remove filtering and include all models of this type.

## See Also

- [var fetchDescriptor: FetchDescriptor<Element>](resultsobserver/fetchdescriptor.md)
  The fetch descriptor used to query the model context.
- [let modelContext: ModelContext](resultsobserver/modelcontext.md)
  The model context from which models are fetched.
- [var sortBy: [SortDescriptor<Element>]](resultsobserver/sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](resultsobserver/sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](resultsobserver/sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](resultsobserver/sectionby.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/filterby)*