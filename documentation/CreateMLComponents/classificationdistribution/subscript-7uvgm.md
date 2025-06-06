# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses a contiguous range of elements.

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
subscript(bounds: Range<Int>) -> Slice<ClassificationDistribution<Label>> { get }
```

## Parameters

- `bounds`: A range of valid indices in the classification distribution.

## See Also

- [subscript(Int) -> Classification<Label>](classificationdistribution/subscript(_:)-856r7.md)
  Accesses a classification at an index.
- [subscript(Label) -> Float?](classificationdistribution/subscript(_:)-s5as.md)
  Accesses a probability with label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:)-7uvgm)*