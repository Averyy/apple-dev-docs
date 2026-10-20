# Additional query macros

**Framework**: SwiftData  
**Role**: API Collection

Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.

## Topics

### Basic queries
- [macro Query(animation: Animation)](./query%28animation%29.md)
  Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>)](./query%28_,animation,sectionby%29-91gkm.md)
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>)](./query%28_,animation,sectionby%29-9futr.md)
- [macro Query(transaction: Transaction)](./query%28transaction%29.md)
  Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28_,transaction,sectionby%29-1poj9.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28_,transaction,sectionby%29-2iol.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,transaction,sectionby%29-4wwsy.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,transaction,sectionby%29-6qrae.md)
### Predicate-based queries
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation)](./query%28filter,sort,animation%29.md)
  Fetches a sorted subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation)](./query%28filter,sort,order,animation%29-80h6f.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation)](./query%28filter,sort,order,animation%29-pb15.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,animation,sectionby%29-1s3xp.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,animation,sectionby%29-82mot.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,order,animation,sectionby%29-132tv.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,order,animation,sectionby%29-66vd3.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,order,animation,sectionby%29-75r20.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,order,animation,sectionby%29-7o0vo.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?)](./query%28filter,sort,transaction%29.md)
  Fetches and sorts the subset of the attached model type that satisfy the specified predicate.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?)](./query%28filter,sort,order,transaction%29-6kkiu.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on a nonoptional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?)](./query%28filter,sort,order,transaction%29-8tk8u.md)
  Fetches a subset of the attached model type, in a specific order, by sorting on an optional attribute.
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,order,transaction,sectionby%29-3cn7t.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,order,transaction,sectionby%29-6c6ho.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,order,transaction,sectionby%29-9mbr6.md)
- [macro Query<Value, Element>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,order,transaction,sectionby%29-i779.md)
### Descriptor-based queries
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation)](./query%28_,animation%29.md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?)](./query%28_,transaction%29.md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.

## See Also

### Model fetch
- [Filtering and sorting persistent data](./filtering-and-sorting-persistent-data.md)
  Manage data store presentation using predicates and dynamic queries.
- [macro Query()](./query%28%29.md)
  Fetches all instances of the attached model type.
- [struct Query](./query.md)
  A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [struct FetchDescriptor](./fetchdescriptor.md)
  A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/additionalquerymacros)*