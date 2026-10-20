# CMTIME_IS_INDEFINITE(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a given time is indefinite.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTIME_IS_INDEFINITE(_ time: CMTime) -> Bool
```

#### Return Value

[`true`](../Swift/true.md) if the time represents an indefinite time; otherwise, [`false`](../Swift/false.md).

## Parameters

- `time`: A time value to test.

## See Also

### Inspecting a Time
- [func CMTimeGetSeconds(CMTime) -> Float64](./cmtimegetseconds%28_%29.md)
  Returns a representation of the time in seconds.
- [func CMTimeAbsoluteValue(CMTime) -> CMTime](./cmtimeabsolutevalue%28_%29.md)
  Returns the absolute value of a time.
- [func CMTIME_IS_VALID(CMTime) -> Bool](./cmtime_is_valid%28_%29.md)
  Returns a Boolean value that indicates whether a given time is valid.
- [func CMTIME_IS_INVALID(CMTime) -> Bool](./cmtime_is_invalid%28_%29.md)
  Returns a Boolean value that indicates whether a given time is invalid.
- [func CMTIME_IS_POSITIVEINFINITY(CMTime) -> Bool](./cmtime_is_positiveinfinity%28_%29.md)
  Returns a Boolean value that indicates whether a given time is positive infinity.
- [func CMTIME_IS_NEGATIVEINFINITY(CMTime) -> Bool](./cmtime_is_negativeinfinity%28_%29.md)
  Returns a Boolean value that indicates whether a given time is negative infinity.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](./cmtime_is_numeric%28_%29.md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](./cmtime_has_been_rounded%28_%29.md)
  Returns a Boolean value that indicates whether the system rounded the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_is_indefinite(_:))*