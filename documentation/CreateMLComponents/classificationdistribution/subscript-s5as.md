# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses a probability with label.

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
subscript(label: Label) -> Float? { get }
```

## Parameters

- `label`: A label in the classification set.

## See Also

- [subscript(Range<Int>) -> Slice<ClassificationDistribution<Label>>](classificationdistribution/subscript(_:)-7uvgm.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> Classification<Label>](classificationdistribution/subscript(_:)-856r7.md)
  Accesses a classification at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:)-s5as)*