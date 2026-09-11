# NDArray.RangeExpression

**Framework**: Core AI  
**Kind**: protocol

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol RangeExpression : Sendable
```

## Topics

### Selecting an entire dimension
- [static var all: _AllRange](ndarray/rangeexpression/all.md)
  A range expression that selects the entire dimension.
### Resolving a range
- [func relative(to: Range<Int>) -> Range<Int>](ndarray/rangeexpression/relative(to:).md)
  Returns Range for the dimension.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rangeexpression)*