# init(lengthLimits:roundingRule:roundingIncrement:)

**Framework**: Swift  
**Kind**: init

Creates a fractional part display strategy that uses the provided behaviors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Range>(lengthLimits: Range, roundingRule: FloatingPointRoundingRule = .toNearestOrEven, roundingIncrement: Double? = nil) where Range : RangeExpression, Range.Bound == Int
```

## Parameters

- `lengthLimits`: The maximum string length of the fractional part.
- `roundingRule`: A rule for rounding fractional values up or down. Defaults to  .
- `roundingIncrement`: A multiple by which the formatter rounds the fractional part. The formatter produces a value that is an even multiple of this increment. If this parameter is   (the default), the formatter doesn’t apply an increment. This value is only meaningful when the combination of allowed units, rounding rule, and formatting strategy requires expressing a unit with a fractional part. For example, a formatter that only allows minutes and uses a strategy with a length of   and default rounding rule formats 40 seconds as  . With a   of  , the formatter formats this value as   instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/init(lengthlimits:roundingrule:roundingincrement:))*