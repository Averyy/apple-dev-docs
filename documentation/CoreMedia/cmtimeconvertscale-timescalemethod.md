# CMTimeConvertScale(_:timescale:method:)

**Framework**: Core Media  
**Kind**: func

Converts the source time to a new timescale using the specified rounding method.

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
func CMTimeConvertScale(_ time: CMTime, timescale newTimescale: Int32, method: CMTimeRoundingMethod) -> CMTime
```

#### Return Value

A time structure that represents the time in a new timescale.

#### Discussion

If this operation needs to round the value, it sets the resulting time’s [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) flag. If the source time is nonnumeric (infinite, indefinite, or invalid), the result is also nonnumeric.

## Parameters

- `time`: The time to convert.
- `newTimescale`: The timescale to use for the converted time.
- `method`: The rounding method to apply.

## See Also

- [enum CMTimeRoundingMethod](cmtimeroundingmethod.md)
  An enumeration of rounding methods to use when performing time calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeconvertscale(_:timescale:method:))*