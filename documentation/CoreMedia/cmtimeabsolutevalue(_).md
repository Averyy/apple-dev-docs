# CMTimeAbsoluteValue(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the absolute value of a time.

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
func CMTimeAbsoluteValue(_ time: CMTime) -> CMTime
```

```c
extern CMTime CMTimeAbsoluteValue(CMTime time);
```

## Return Value

The time value, but with its sign inverted, if necessary.

## Parameters

- `time`: A time structure.

## See Also

### Inspecting a Time
- [func CMTimeGetSeconds(CMTime) -> Float64](./cmtimegetseconds%28_%29.md)
  Returns a representation of the time in seconds.
- [func CMTIME_IS_VALID(CMTime) -> Bool](./cmtime_is_valid%28_%29.md)
  Returns a Boolean value that indicates whether a given time is valid.
- [func CMTIME_IS_INVALID(CMTime) -> Bool](./cmtime_is_invalid%28_%29.md)
  Returns a Boolean value that indicates whether a given time is invalid.
- [func CMTIME_IS_POSITIVEINFINITY(CMTime) -> Bool](./cmtime_is_positiveinfinity%28_%29.md)
  Returns a Boolean value that indicates whether a given time is positive infinity.
- [func CMTIME_IS_NEGATIVEINFINITY(CMTime) -> Bool](./cmtime_is_negativeinfinity%28_%29.md)
  Returns a Boolean value that indicates whether a given time is negative infinity.
- [func CMTIME_IS_INDEFINITE(CMTime) -> Bool](./cmtime_is_indefinite%28_%29.md)
  Returns a Boolean value that indicates whether a given time is indefinite.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](./cmtime_is_numeric%28_%29.md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](./cmtime_has_been_rounded%28_%29.md)
  Returns a Boolean value that indicates whether the system rounded the time value.
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
- [CMTIME_IS_NUMERIC](./cmtime_is_numeric.md)
  Returns a Boolean value that indicates whether a time is numeric.
- [CMTIME_HAS_BEEN_ROUNDED](./cmtime_has_been_rounded.md)
  Returns a Boolean value that indicates whether the system rounded the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeabsolutevalue(_:))*