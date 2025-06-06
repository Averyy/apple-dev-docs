# CMTimeMultiplyByFloat64(_:multiplier:)

**Framework**: Core Media  
**Kind**: func

Returns the result of multiplying a time by a floating-point multiplier.

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
func CMTimeMultiplyByFloat64(_ time: CMTime, multiplier: Float64) -> CMTime
```

#### Return Value

A time structure that represents the product of the multiplied time.

#### Discussion

The result has the same timescale as the passed time argument. If the result’s timescale is less than `65536`, the system repeatedly doubles it until it’s at least that value. If the result overflows, the system repeatedly halves the result until no overflow occurs. The system applies the default rounding method when converting the result to this timescale. If the result’s value still overflows when its timescale is `1`, then the result is positive or negative infinity, depending on the direction of the overflow. If rounding occurs for any reason, the system sets the result’s [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) flag. It also sets this flag if the time argument has [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) set. If the `time` operand is invalid, the result is invalid. If the time operand is valid but infinite, the result is infinite and of an appropriate sign, based on the signs of both operands. If the time operand is valid, but indefinite, the result is indefinite.

## Parameters

- `time`: A time value to multiply.
- `multiplier`: A 64-bit floating-point multiplier value.

## See Also

- [func CMTimeAdd(CMTime, CMTime) -> CMTime](cmtimeadd(_:_:).md)
  Returns the sum of two times.
- [func CMTimeSubtract(CMTime, CMTime) -> CMTime](cmtimesubtract(_:_:).md)
  Returns the difference between two times.
- [func CMTimeMultiply(CMTime, multiplier: Int32) -> CMTime](cmtimemultiply(_:multiplier:).md)
  Returns the result of multiplying a time by an integer multiplier.
- [func CMTimeMultiplyByRatio(CMTime, multiplier: Int32, divisor: Int32) -> CMTime](cmtimemultiplybyratio(_:multiplier:divisor:).md)
  Returns the result of multiplying a time by an integer multiplier, and then dividing the result by the divisor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemultiplybyfloat64(_:multiplier:))*