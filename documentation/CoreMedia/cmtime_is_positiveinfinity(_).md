# CMTIME_IS_POSITIVEINFINITY(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a given time is positive infinity.

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
func CMTIME_IS_POSITIVEINFINITY(_ time: CMTime) -> Bool
```

## Return Value

[`true`](../Swift/true.md) if the time represents positive infinity; otherwise, [`false`](../Swift/false.md).

## Discussion

Use this macro instead of testing if a time is equal to [`positiveInfinity`](./cmtime/positiveinfinity.md), because there are many times that represent positive infinity. This is because the system ignores nonflags fields, so they can contain anything.

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
- [func CMTIME_IS_NEGATIVEINFINITY(CMTime) -> Bool](./cmtime_is_negativeinfinity%28_%29.md)
  Returns a Boolean value that indicates whether a given time is negative infinity.
- [func CMTIME_IS_INDEFINITE(CMTime) -> Bool](./cmtime_is_indefinite%28_%29.md)
  Returns a Boolean value that indicates whether a given time is indefinite.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](./cmtime_is_numeric%28_%29.md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](./cmtime_has_been_rounded%28_%29.md)
  Returns a Boolean value that indicates whether the system rounded the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_is_positiveinfinity(_:))*