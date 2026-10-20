# init(_:transaction:)

**Framework**: SwiftData  
**Kind**: init  
**Role**: Initializer

Create a query with a SwiftData fetch descriptor.

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
@preconcurrency init(_ descriptor: FetchDescriptor<Element>, transaction: Transaction? = nil) where Result == [Element]
```

## Parameters

- `descriptor`: A `SwiftData.FetchDescriptor`.
- `transaction`: A transaction to use for user interface changes that result from changes to the fetched results.

## See Also

### Creating a query
- [init(FetchDescriptor<Element>, animation: Animation)](./init%28_,animation%29.md)
  Create a query with a SwiftData fetch descriptor.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](./init%28filter,sort,animation%29.md)
  Create a query with a predicate, and a list of sort descriptors.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](./init%28filter,sort,order,animation%29-1qfoj.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](./init%28filter,sort,order,animation%29-3qovd.md)
  Creates a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](./init%28filter,sort,transaction%29.md)
  Create a query with a predicate, and a list of sort descriptors.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](./init%28filter,sort,order,transaction%29-2bx9a.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](./init%28filter,sort,order,transaction%29-8q7vs.md)
  Create a query with a predicate, a key path to a property for sorting, and the order to sort by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(_:transaction:))*