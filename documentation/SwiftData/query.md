# Query

**Framework**: SwiftData  
**Kind**: struct

A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Query<Element, Result> where Element : PersistentModel
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

## Topics

### Creating a query
- [init(FetchDescriptor<Element>, animation: Animation)](query/init(_:animation:).md)
  Create a query with a SwiftData fetch descriptor.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](query/init(filter:sort:animation:).md)
  Create a query with a predicate, and a list of sort descriptors.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](query/init(filter:sort:order:animation:)-1qfoj.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](query/init(filter:sort:order:animation:)-3qovd.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(FetchDescriptor<Element>, transaction: Transaction?)](query/init(_:transaction:).md)
  Create a query with a SwiftData fetch descriptor.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](query/init(filter:sort:transaction:).md)
  Create a query with a predicate, and a list of sort descriptors.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](query/init(filter:sort:order:transaction:)-2bx9a.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](query/init(filter:sort:order:transaction:)-8q7vs.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
### Creating an unsorted, sectioned query
- [init(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(_:animation:sectionby:)-2em2m.md)
  Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path.
- [init(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(_:animation:sectionby:)-2pqhv.md)
  Creates a sectioned query from a fetch descriptor, grouped by an optional String key path.
- [init(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(_:transaction:sectionby:)-5814o.md)
  Creates a sectioned query from a fetch descriptor, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(_:transaction:sectionby:)-9sb87.md)
  Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. Pass `nil` to disable sectioning.
### Creating a sorted, sectioned query
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:animation:sectionby:)-5wk67.md)
  Creates a sectioned query with sort descriptors, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:animation:sectionby:)-8e78r.md)
  Creates a sectioned query with sort descriptors, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-2e9oh.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-2e9oh.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-4pdmu.md)
  Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:animation:sectionby:)-6b4tq.md)
  Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:animation:sectionby:)-7d51r.md)
  Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:transaction:sectionby:)-5ym3e.md)
  Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:transaction:sectionby:)-8hx6i.md)
  Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:transaction:sectionby:)-930wx.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:transaction:sectionby:)-l6d4.md)
  Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:transaction:sectionby:)-2b0zd.md)
  Creates a sectioned query with sort descriptors, grouped into sections by a String key path.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:transaction:sectionby:)-965mg.md)
  Creates a sectioned query with sort descriptors, grouped by an optional String key path.
### Getting query configuration
- [var modelContext: ModelContext](query/modelcontext.md)
  Current model context `Query` interacts with.
- [var fetchError: (any Error)?](query/fetcherror.md)
  An error encountered during the most recent attempt to fetch data.
### Accessing the value
- [var wrappedValue: Result](query/wrappedvalue.md)
  The most recent fetched result from the Query.
### Accessing sections
- [var sections: ResultsSectionCollection<Element, String>](query/sections.md)
  The sections computed from the current results, grouped by the `sectionBy` key path.
- [struct ResultsSectionCollection](resultssectioncollection.md)
  A collection of sections as returned by [`sections`](resultsobserver/sections.md) or `Query.sections`.

## Relationships

### Conforms To
- [DynamicProperty](../SwiftUI/DynamicProperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md)
  Manage data store presentation using predicates and dynamic queries.
- [macro Query()](query().md)
  Fetches all instances of the attached model type.
- [Additional query macros](additionalquerymacros.md)
  Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [struct FetchDescriptor](fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query)*