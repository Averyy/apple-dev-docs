# NDArray.RangeExpression

**Framework**: Core AI  
**Kind**: protocol  
**Role**: Protocol

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
- [static var all: _AllRange](./rangeexpression/all.md)
  A range expression that selects the entire dimension.
### Resolving a range
- [func relative(to: Range<Int>) -> Range<Int>](./rangeexpression/relative%28to%29.md)
  Returns Range for the dimension.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rangeexpression)*