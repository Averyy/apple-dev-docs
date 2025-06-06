# JointTransforms.Iterator

**Framework**: RealityKit  
**Kind**: typealias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
typealias Iterator = IndexingIterator<JointTransforms>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## See Also

- [JointTransforms.ArrayLiteralElement](jointtransforms/arrayliteralelement.md)
  The type of the elements of an array literal.
- [JointTransforms.Element](jointtransforms/element.md)
  An individual joint transform in the collection.
- [JointTransforms.Index](jointtransforms/index.md)
  A position of an individual joint transform in the collection.
- [JointTransforms.Indices](jointtransforms/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [JointTransforms.SubSequence](jointtransforms/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/iterator)*