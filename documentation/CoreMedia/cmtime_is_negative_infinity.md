# CMTIME_IS_NEGATIVE_INFINITY

**Framework**: Core Media  
**Kind**: macro  
**Role**: Macro

Returns a Boolean value that indicates whether a time is negative infinity.

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
#define CMTIME_IS_NEGATIVE_INFINITY(time)
```

#### Return Value

[`true`](../Swift/true.md) if the time is negative infinity; otherwise, [`false`](../Swift/false.md).

#### Discussion

Use this macro instead of testing whether a time is equal to [`negativeInfinity`](./cmtime/negativeinfinity.md), because there are many times that represent negative infinity. The system ignores nonflags fields, so they can contain anything.

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
- [CMTIME_IS_INDEFINITE](./cmtime_is_indefinite.md)
  Returns a Boolean value that indicates whether a time is indefinite.
- [CMTIME_IS_NUMERIC](./cmtime_is_numeric.md)
  Returns a Boolean value that indicates whether a time is numeric.
- [CMTIME_HAS_BEEN_ROUNDED](./cmtime_has_been_rounded.md)
  Returns a Boolean value that indicates whether the system rounded the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_is_negative_infinity)*