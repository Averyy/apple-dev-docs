# Query(filter:sort:order:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: macro

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
@attached
(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Value, Element>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value>, order: SortOrder = .forward, transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String?>) where Value : Comparable, Element : PersistentModel
```

## See Also

- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](query(filter:sort:animation:).md)
  Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](query(filter:sort:order:animation:)-80h6f.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(filter:sort:order:transaction:sectionby:)-i779)*