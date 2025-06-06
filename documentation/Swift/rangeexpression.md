# RangeExpression

**Framework**: Swift  
**Kind**: protocol

A type that can be used to slice a collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol RangeExpression<Bound>
```

#### Overview

A type that conforms to `RangeExpression` can convert itself to a `Range<Bound>` of indices within a given collection.

## Topics

### Operators
- [static func ~= (Self, Self.Bound) -> Bool](rangeexpression/~=(_:_:).md)
  Returns a Boolean value indicating whether a value is included in a range.
### Associated Types
- [associatedtype Bound : Comparable](rangeexpression/bound.md)
  The type for which the expression describes a range.
### Instance Methods
- [func contains(Self.Bound) -> Bool](rangeexpression/contains(_:).md)
  Returns a Boolean value indicating whether the given element is contained within the range expression.
- [func relative<C>(to: C) -> Range<Self.Bound>](rangeexpression/relative(to:).md)
  Returns the range of indices described by this range expression within the given collection.

## Relationships

### Conforming Types
- [ClosedRange](closedrange.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [Range](range.md)

## See Also

- [struct PartialRangeUpTo](partialrangeupto.md)
  A partial half-open interval up to, but not including, an upper bound.
- [struct PartialRangeThrough](partialrangethrough.md)
  A partial interval up to, and including, an upper bound.
- [struct PartialRangeFrom](partialrangefrom.md)
  A partial interval extending upward from a lower bound.
- [enum UnboundedRange_](unboundedrange_.md)
  A range expression that represents the entire range of a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeexpression)*