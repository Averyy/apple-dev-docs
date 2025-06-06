# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses a classification at an index.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
subscript(index: Int) -> Classification<Label> { get }
```

## Parameters

- `index`: A valid index to a classification in the classification distribution.

## See Also

- [subscript(Range<Int>) -> Slice<ClassificationDistribution<Label>>](classificationdistribution/subscript(_:)-7uvgm.md)
  Accesses a contiguous range of elements.
- [subscript(Label) -> Float?](classificationdistribution/subscript(_:)-s5as.md)
  Accesses a probability with label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:)-856r7)*