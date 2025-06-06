# CMTimeAbsoluteValue(_:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

The time value, but with its sign inverted, if necessary.

## Parameters

- `time`: A time structure.

## See Also

- [func CMTimeGetSeconds(CMTime) -> Float64](cmtimegetseconds(_:).md)
  Returns a representation of the time in seconds.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeabsolutevalue(_:))*