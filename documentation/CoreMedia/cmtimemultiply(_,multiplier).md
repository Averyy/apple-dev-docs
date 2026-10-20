# CMTimeMultiply(_:multiplier:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the result of multiplying a time by an integer multiplier.

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
func CMTimeMultiply(_ time: CMTime, multiplier: Int32) -> CMTime
```

```c
extern CMTime CMTimeMultiply(CMTime time, int32_t multiplier);
```

#### Return Value

A time structure that represents the product of the multiplied time.

#### Discussion

The result has the same timescale as the time argument. If the result overflows, the system repeatedly halves the result until no overflow occurs. The system applies the default rounding method when converting the result to this timescale. If the result’s value still overflows when its timescale is `1`, then the result is positive or negative infinity, depending on the direction of the overflow. If rounding occurs for any reason, the system sets the result’s [`hasBeenRounded`](./cmtimeflags/hasbeenrounded.md) flag. It also sets this flag if the time argument has [`hasBeenRounded`](./cmtimeflags/hasbeenrounded.md) set. If the `time` operand is invalid, the result is invalid. If the time operand is valid but infinite, the result is infinite and of an appropriate sign, based on the signs of both operands. If the time operand is valid, but indefinite, the result is indefinite.

## Parameters

- `time`: A time value to multiply.
- `multiplier`: A 32-bit integer multiplier value.

## See Also

### Performing Time Calculations
- [func CMTimeAdd(CMTime, CMTime) -> CMTime](./cmtimeadd%28_,_%29.md)
  Returns the sum of two times.
- [func CMTimeSubtract(CMTime, CMTime) -> CMTime](./cmtimesubtract%28_,_%29.md)
  Returns the difference between two times.
- [func CMTimeMultiplyByFloat64(CMTime, multiplier: Float64) -> CMTime](./cmtimemultiplybyfloat64%28_,multiplier%29.md)
  Returns the result of multiplying a time by a floating-point multiplier.
- [func CMTimeMultiplyByRatio(CMTime, multiplier: Int32, divisor: Int32) -> CMTime](./cmtimemultiplybyratio%28_,multiplier,divisor%29.md)
  Returns the result of multiplying a time by an integer multiplier, and then dividing the result by the divisor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemultiply(_:multiplier:))*