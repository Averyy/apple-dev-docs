# CMTIME_IS_NUMERIC

**Framework**: Core Media  
**Kind**: macro  
**Role**: Macro

Returns a Boolean value that indicates whether a time is numeric.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define CMTIME_IS_NUMERIC(time)
```

#### Return Value

[`true`](../Swift/true.md) if the time is numeric; otherwise, [`false`](../Swift/false.md).

#### Discussion

A numeric time contains a usable [`value`](./cmtime/value.md), [`timescale`](./cmtime/timescale.md), and [`epoch`](./cmtime/epoch.md).

## See Also

### Inspecting a Time
- [func CMTimeGetSeconds(CMTime) -> Float64](./cmtimegetseconds%28_%29.md)
  Returns a representation of the time in seconds.
- [func CMTimeAbsoluteValue(CMTime) -> CMTime](./cmtimeabsolutevalue%28_%29.md)
  Returns the absolute value of a time.
- [CMTIME_IS_VALID](./cmtime_is_valid.md)
  Returns a Boolean value that indicates whether a time is valid.
- [CMTIME_IS_INVALID](./cmtime_is_invalid.md)
  Returns a Boolean value that indicates whether a time is invalid.
- [CMTIME_IS_POSITIVE_INFINITY](./cmtime_is_positive_infinity.md)
  Returns a Boolean value that indicates whether a time is positive infinity.
- [CMTIME_IS_NEGATIVE_INFINITY](./cmtime_is_negative_infinity.md)
  Returns a Boolean value that indicates whether a time is negative infinity.
- [CMTIME_IS_INDEFINITE](./cmtime_is_indefinite.md)
  Returns a Boolean value that indicates whether a time is indefinite.
- [CMTIME_HAS_BEEN_ROUNDED](./cmtime_has_been_rounded.md)
  Returns a Boolean value that indicates whether the system rounded the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_is_numeric)*