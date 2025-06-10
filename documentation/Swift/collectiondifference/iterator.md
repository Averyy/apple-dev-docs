# CollectionDifference.Iterator

**Framework**: Swift  
**Kind**: typealias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias Iterator = IndexingIterator<CollectionDifference<ChangeElement>>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/iterator)*