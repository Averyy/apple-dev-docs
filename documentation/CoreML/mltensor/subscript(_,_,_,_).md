# subscript(_:_:_:_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

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
subscript(firstRange: (any MLTensorRangeExpression)?, secondRange: (any MLTensorRangeExpression)?, thirdRange: UnboundedRange, trailingRanges: (any MLTensorRangeExpression)?...) -> MLTensor { get }
```

## See Also

### Accessing a multiarray’s elements
- [subscript((any MLTensorRangeExpression)?...) -> MLTensor](./subscript%28_%29.md)
- [subscript(UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./subscript%28_,_%29.md)
- [subscript((any MLTensorRangeExpression)?, UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./subscript%28_,_,_%29.md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./subscript%28_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/subscript(_:_:_:_:))*