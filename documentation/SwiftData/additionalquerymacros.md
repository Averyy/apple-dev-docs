# Additional query macros

**Framework**: SwiftData

Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.

## Topics

### Basic queries
- [macro Query(animation: Animation)](query(animation:).md)
  Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>)](query(_:animation:sectionby:)-91gkm.md)
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>)](query(_:animation:sectionby:)-9futr.md)
- [macro Query(transaction: Transaction)](query(transaction:).md)
  Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(_:transaction:sectionby:)-1poj9.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(_:transaction:sectionby:)-2iol.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:transaction:sectionby:)-4wwsy.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(filter:sort:transaction:sectionby:)-6qrae.md)
### Predicate-based queries
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
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:order:transaction:sectionby:)-i779.md)
### Descriptor-based queries
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation)](query(_:animation:).md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?)](query(_:transaction:).md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.

## See Also

- [Filtering and sorting persistent data](filtering-and-sorting-persistent-data.md)
  Manage data store presentation using predicates and dynamic queries.
- [macro Query()](query().md)
  Fetches all instances of the attached model type.
- [struct Query](query.md)
  A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [struct FetchDescriptor](fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/additionalquerymacros)*