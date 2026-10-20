# Query(filter:sort:order:animation:)

**Framework**: SwiftData  
**Kind**: macro

Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.

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
(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Value, Element>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value>, order: SortOrder = .forward, animation: Animation) where Value : Comparable, Element : PersistentModel
```

## Parameters

- `filter`: The logical condition the query uses to determine if it returns a specific model instance.
- `keyPath`: The keypath of the nonoptional attribute to sort by.
- `order`: The order of the sort.
- `animation`: The animation to use when updates to the fetched models trigger user interface changes.

## See Also

- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](query(filter:sort:animation:).md)
  Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-pb15.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String?>)](query(filter:sort:animation:sectionby:)-1s3xp.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String>)](query(filter:sort:animation:sectionby:)-82mot.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>)](query(filter:sort:order:animation:sectionby:)-132tv.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>)](query(filter:sort:order:animation:sectionby:)-66vd3.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>)](query(filter:sort:order:animation:sectionby:)-75r20.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>)](query(filter:sort:order:animation:sectionby:)-7o0vo.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](query(filter:sort:transaction:).md)
  Fetches and sorts the subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-6kkiu.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](query(filter:sort:order:transaction:)-8tk8u.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(filter:sort:order:transaction:sectionby:)-3cn7t.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(filter:sort:order:transaction:sectionby:)-6c6ho.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:order:transaction:sectionby:)-9mbr6.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:order:transaction:sectionby:)-i779.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(filter:sort:order:animation:)-80h6f)*