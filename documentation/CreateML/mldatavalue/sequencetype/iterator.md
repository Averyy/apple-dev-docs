# MLDataValue.SequenceType.Iterator

**Framework**: Create ML  
**Kind**: typealias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias Iterator = IndexingIterator<MLDataValue.SequenceType>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/iterator)*