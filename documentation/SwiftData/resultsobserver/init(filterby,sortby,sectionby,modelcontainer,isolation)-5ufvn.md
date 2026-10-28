# init(filterBy:sortBy:sectionBy:modelContainer:isolation:)

**Framework**: SwiftData  
**Kind**: init  
**Role**: Initializer

Creates a new observer with individual filter and sort criteria, a String section key path, and a model container.

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
convenience init(filterBy: Predicate<Element>? = nil, sortBy: [SortDescriptor<Element>]? = nil, sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)? = #isolation) throws
```

Available when `Element` conforms to `PersistentModel` and `SectionTitle` is `String`.

## Discussion

> **Throws**: An error if the initial fetch fails.

## Parameters

- `filterBy`: An optional predicate to filter the results.
- `sortBy`: An optional array of sort descriptors to order the results.
- `sectionBy`: A key path on the element type that returns the section name.
- `modelContainer`: The model container from which a new context will be created.

## See Also

### Creating a results observer with a predicate
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](./init%28filterby,sortby,modelcontext,isolation%29.md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](./init%28filterby,sortby,sectionby,modelcontext,isolation%29-4ainb.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](./init%28filterby,sortby,sectionby,modelcontext,isolation%29-gsuz.md)
  Creates a new observer with individual filter and sort criteria, a String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](./init%28filterby,sortby,modelcontainer,isolation%29.md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model container.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](./init%28filterby,sortby,sectionby,modelcontainer,isolation%29-9lfy0.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/init(filterby:sortby:sectionby:modelcontainer:isolation:)-5ufvn)*