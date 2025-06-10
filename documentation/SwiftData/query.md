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
### Getting query configuration
- [var modelContext: ModelContext](query/modelcontext.md)
  Current model context `Query` interacts with.
- [var fetchError: (any Error)?](query/fetcherror.md)
  An error encountered during the most recent attempt to fetch data.
### Accessing the value
- [var wrappedValue: Result](query/wrappedvalue.md)
  The most recent fetched result from the Query.
### Updating the value
- [func update()](query/update.md)
  Updates the underlying value of the stored value.

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
- [macro Query(animation: Animation)](query(animation:).md)
  Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation)](query(_:animation:).md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](query(filter:sort:animation:).md)
  Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-80h6f.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-pb15.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query(transaction: Transaction)](query(transaction:).md)
  Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?)](query(_:transaction:).md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](query(filter:sort:transaction:).md)
  Fetches and sorts the subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-6kkiu.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-8tk8u.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [struct FetchDescriptor](fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query)*