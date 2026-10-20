# Query(animation:)

**Framework**: SwiftData  
**Kind**: macro  
**Role**: Macro

Fetches all instances of the attached model type, using the specified animation to animate any subsequent changes.

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
(accessor) @attached(peer, names: prefixed(`_`)) macro Query(animation: Animation)
```

## Parameters

- `animation`: The animation to use when updates to the fetched models trigger user interface changes.

## See Also

### Basic queries
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>)](./query%28_,animation,sectionby%29-91gkm.md)
- [macro Query<Element>(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>)](./query%28_,animation,sectionby%29-9futr.md)
- [macro Query(transaction: Transaction)](./query%28transaction%29.md)
  Fetches all instances of the attached model type, using the specified transaction to animate any subsequent changes.
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28_,transaction,sectionby%29-1poj9.md)
- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28_,transaction,sectionby%29-2iol.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>)](./query%28filter,sort,transaction,sectionby%29-4wwsy.md)
- [macro Query<Element>(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>)](./query%28filter,sort,transaction,sectionby%29-6qrae.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(animation:))*