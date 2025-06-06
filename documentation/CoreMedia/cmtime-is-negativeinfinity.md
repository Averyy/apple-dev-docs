# CMTIME_IS_NEGATIVEINFINITY(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a given time is negative infinity.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst ?+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTIME_IS_NEGATIVEINFINITY(_ time: CMTime) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the time represents negative infinity; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Use this macro instead of testing whether a time is equal to [`negativeInfinity`](cmtime/negativeinfinity.md), because there are many times that negative positive infinity. This is because the system ignores nonflags fields, so they can contain anything.

## Parameters

- `time`: A time value to test.

## See Also

- [func CMTimeGetSeconds(CMTime) -> Float64](cmtimegetseconds(_:).md)
  Returns a representation of the time in seconds.
- [func CMTimeAbsoluteValue(CMTime) -> CMTime](cmtimeabsolutevalue(_:).md)
  Returns the absolute value of a time.
- [func CMTIME_IS_VALID(CMTime) -> Bool](cmtime_is_valid(_:).md)
  Returns a Boolean value that indicates whether a given time is valid.
- [func CMTIME_IS_INVALID(CMTime) -> Bool](cmtime_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a given time is invalid.
- [func CMTIME_IS_POSITIVEINFINITY(CMTime) -> Bool](cmtime_is_positiveinfinity(_:).md)
  Returns a Boolean value that indicates whether a given time is positive infinity.
- [func CMTIME_IS_INDEFINITE(CMTime) -> Bool](cmtime_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a given time is indefinite.
- [func CMTIME_IS_NUMERIC(CMTime) -> Bool](cmtime_is_numeric(_:).md)
  Returns a Boolean value that indicates whether a given time is numeric.
- [func CMTIME_HAS_BEEN_ROUNDED(CMTime) -> Bool](cmtime_has_been_rounded(_:).md)
  Returns a Boolean value that indicates whether the system rounded the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_is_negativeinfinity(_:))*