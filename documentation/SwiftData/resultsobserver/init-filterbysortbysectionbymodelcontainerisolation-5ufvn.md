# init(filterBy:sortBy:sectionBy:modelContainer:isolation:)

**Framework**: SwiftData  
**Kind**: init

Creates a new observer with individual filter and sort criteria, a String section key path, and a model container.

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
convenience init(filterBy: Predicate<Element>? = nil, sortBy: [SortDescriptor<Element>]? = nil, sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)? = #isolation) throws
```

#### Discussion

> **Note**: An error if the initial fetch fails.

## Parameters

- `filterBy`: An optional predicate to filter the results.
- `sortBy`: An optional array of sort descriptors to order the results.
- `sectionBy`: A key path on the element type that returns the section name.
- `modelContainer`: The model container from which a new context will be created.

## See Also

- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:modelcontext:isolation:).md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontext:isolation:)-4ainb.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontext:isolation:)-gsuz.md)
  Creates a new observer with individual filter and sort criteria, a String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:modelcontainer:isolation:).md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model container.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontainer:isolation:)-9lfy0.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/init(filterby:sortby:sectionby:modelcontainer:isolation:)-5ufvn)*