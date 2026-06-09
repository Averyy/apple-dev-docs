# NDArray.RangeExpression

**Framework**: Core AI  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol RangeExpression : Sendable
```

## Topics

### Instance Methods
- [func relative(to: Range<Int>) -> Range<Int>](ndarray/rangeexpression/relative(to:).md)
  Returns Range for the dimension.
### Type Properties
- [static var all: _AllRange](ndarray/rangeexpression/all.md)
  A range expression that selects the entire dimension.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rangeexpression)*