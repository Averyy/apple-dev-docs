# Int32.Words.Iterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias Iterator = IndexingIterator<Int32.Words>
```

## Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/words-swift.struct/iterator)*