# Query(transaction:)

**Framework**: SwiftData  
**Kind**: macro

Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.

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
(accessor) @attached(peer, names: prefixed(`_`)) macro Query(transaction: Transaction)
```

## Parameters

- `transaction`: The transaction to use when updates to the fetched models trigger user interface changes.

## See Also

- [macro Query(animation: Animation)](query(animation:).md)
  Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>)](query(_:animation:sectionby:)-91gkm.md)
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>)](query(_:animation:sectionby:)-9futr.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(_:transaction:sectionby:)-1poj9.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(_:transaction:sectionby:)-2iol.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:transaction:sectionby:)-4wwsy.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(filter:sort:transaction:sectionby:)-6qrae.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(transaction:))*