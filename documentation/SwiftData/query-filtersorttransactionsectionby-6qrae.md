# Query(filter:sort:transaction:sectionBy:)

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
(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String>) where Element : PersistentModel
```

## See Also

- [macro Query(animation: Animation)](query(animation:).md)
  Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>)](query(_:animation:sectionby:)-91gkm.md)
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>)](query(_:animation:sectionby:)-9futr.md)
- [macro Query(transaction: Transaction)](query(transaction:).md)
  Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](query(_:transaction:sectionby:)-1poj9.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(_:transaction:sectionby:)-2iol.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](query(filter:sort:transaction:sectionby:)-4wwsy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(filter:sort:transaction:sectionby:)-6qrae)*