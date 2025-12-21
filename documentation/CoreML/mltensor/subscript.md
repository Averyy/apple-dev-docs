# subscript(_:_:_:_:_:)

**Framework**: Core ML  
**Kind**: subscript

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
subscript(firstRange: (any MLTensorRangeExpression)?, secondRange: (any MLTensorRangeExpression)?, thirdRange: (any MLTensorRangeExpression)?, fourthRange: (UnboundedRange_) -> (), trailingRanges: (any MLTensorRangeExpression)?...) -> MLTensor { get }
```

## See Also

- [subscript((any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:).md)
- [subscript((UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:).md)
- [subscript((any MLTensorRangeExpression)?, (UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:_:).md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/subscript(_:_:_:_:_:))*