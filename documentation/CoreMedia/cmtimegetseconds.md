# CMTimeGetSeconds(_:)

**Framework**: Core Media  
**Kind**: func

Returns a representation of the time in seconds.

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
func CMTimeGetSeconds(_ time: CMTime) -> Float64
```

#### Return Value

The time in seconds.

#### Discussion

If the time is [`invalid`](cmtime/invalid.md) or [`indefinite`](cmtime/indefinite.md), the result is [`nan`](https://developer.apple.com/documentation/Swift/Double/nan).

If the time is infinite, the result is positive or negative infinity.

If the time is numeric, it ignores the epoch, and returns the result of `time.value / time.timescale`. It performs the division in `Float64`, so the fraction isn’t lost in the returned result.

## Parameters

- `time`: A time value for which to retrieve seconds.

## See Also

- [func CMTimeAbsoluteValue(CMTime) -> CMTime](cmtimeabsolutevalue(_:).md)
  Returns the absolute value of a time.
- [func CMTIME_IS_VALID(CMTime) -> Bool](cmtime_is_valid(_:).md)
  Returns a Boolean value that indicates whether a given time is valid.
- [func CMTIME_IS_INVALID(CMTime) -> Bool](cmtime_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a given time is invalid.
- [func CMTIME_IS_POSITIVEINFINITY(CMTime) -> Bool](cmtime_is_positiveinfinity(_:).md)
  Returns a Boolean value that indicates whether a given time is positive infinity.
- [func CMTIME_IS_NEGATIVEINFINITY(CMTime) -> Bool](cmtime_is_negativeinfinity(_:).md)
  Returns a Boolean value that indicates whether a given time is negative infinity.
- [func CMTIME_IS_INDEFINITE(CMTime) -> Bool](cmtime_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a given time is indefinite.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](cmtime_is_numeric(_:).md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](cmtime_has_been_rounded(_:).md)
  Returns a Boolean value that indicates whether the system rounded the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimegetseconds(_:))*