# Query(filter:sort:transaction:)

**Framework**: SwiftData  
**Kind**: macro

Fetches and sorts the subset of the attached model type that satisfy the specified predicate.

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
@attached
(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil) where Element : PersistentModel
```

## Parameters

- `filter`: The logical condition the query uses to determine if it returns a specific model instance.
- `descriptors`: An array of sort descriptors to use when arranging the fetched models.
- `transaction`: The transaction to use when updates to the fetched models trigger user interface changes.

## See Also

- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](query(filter:sort:animation:).md)
  Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-80h6f.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-pb15.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-6kkiu.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-8tk8u.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(filter:sort:transaction:))*