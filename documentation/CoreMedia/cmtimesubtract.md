# CMTimeSubtract(_:_:)

**Framework**: Core Media  
**Kind**: func

Returns the difference between two times.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeSubtract(_ lhs: CMTime, _ rhs: CMTime) -> CMTime
```

#### Return Value

A time value that represents the result of the operation.

#### Discussion

If the operands have the same timescale, the timescale of the result is the same as the operands’ timescale. If the operands have different timescales, the timescale of the result is the least common multiple of the operands’ timescales. If that LCM timescale is greater than [`kCMTimeMaxTimescale`](kcmtimemaxtimescale.md), the result timescale is [`kCMTimeMaxTimescale`](kcmtimemaxtimescale.md), and the system applies the default rounding when it converts the result to this timescale.

If the value of the result overflows, the system repeatedly halves its timescale until it no longer overflows, and uses the default rounding to convert the result to this timescale. If the result’s value still overflows when its timescale is `1`, the system sets the result’s timescale to positive or negative infinity, depending on the direction of the overflow. If any rounding occurs, or if either operand has its [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) flag set, the system sets the result’s [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) flag.

If either operand is invalid, the result is invalid. If the operands are valid, but one is infinite, the result is infinite. If the operands are valid, and both are infinite, the results are as follows:

- +infinity - +infinity == invalid
- -infinity - -infinity == invalid
- +infinity - -infinity == +infinity
- -infinity + +infinity == invalid

If the operands are valid, not infinite, and either or both is [`indefinite`](cmtime/indefinite.md), the result is [`indefinite`](cmtime/indefinite.md).

If the two operands are numeric, but have different nonzero epochs, the result is [`invalid`](cmtime/invalid.md). If both have the same nonzero epoch, the result is epoch zero. You can’t add or subtract times that have different epochs, because the epoch length is unknown. The system considers times in epoch zero to be durations, so you can add them to times in other epochs. You can compare times in different epochs, however, because numerically greater epochs always occur after numerically lesser epochs.

## Parameters

- `lhs`: A time value.
- `rhs`: A time value to subtract from the minuend.

## See Also

- [func CMTimeAdd(CMTime, CMTime) -> CMTime](cmtimeadd(_:_:).md)
  Returns the sum of two times.
- [func CMTimeMultiply(CMTime, multiplier: Int32) -> CMTime](cmtimemultiply(_:multiplier:).md)
  Returns the result of multiplying a time by an integer multiplier.
- [func CMTimeMultiplyByFloat64(CMTime, multiplier: Float64) -> CMTime](cmtimemultiplybyfloat64(_:multiplier:).md)
  Returns the result of multiplying a time by a floating-point multiplier.
- [func CMTimeMultiplyByRatio(CMTime, multiplier: Int32, divisor: Int32) -> CMTime](cmtimemultiplybyratio(_:multiplier:divisor:).md)
  Returns the result of multiplying a time by an integer multiplier, and then dividing the result by the divisor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimesubtract(_:_:))*