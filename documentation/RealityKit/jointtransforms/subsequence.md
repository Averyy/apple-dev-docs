# JointTransforms.SubSequence

**Framework**: RealityKit  
**Kind**: typealias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
typealias SubSequence = Slice<JointTransforms>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

## See Also

- [JointTransforms.ArrayLiteralElement](jointtransforms/arrayliteralelement.md)
  The type of the elements of an array literal.
- [JointTransforms.Element](jointtransforms/element.md)
  An individual joint transform in the collection.
- [JointTransforms.Index](jointtransforms/index.md)
  A position of an individual joint transform in the collection.
- [JointTransforms.Indices](jointtransforms/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [JointTransforms.Iterator](jointtransforms/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms/subsequence)*