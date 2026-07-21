# NDArray.RangeExpression

**Framework**: Core AI  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rangeexpression)*