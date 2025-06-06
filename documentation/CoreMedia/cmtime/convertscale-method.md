# convertScale(_:method:)

**Framework**: Core Media  
**Kind**: method

Converts the source time to a new timescale using the specified rounding method.

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
func convertScale(_ newTimescale: Int32, method: CMTimeRoundingMethod) -> CMTime
```

#### Return Value

A converted time value.

## Parameters

- `newTimescale`: The timescale to use for the converted time.
- `method`: The rounding method to apply.

## See Also

- [enum CMTimeRoundingMethod](cmtimeroundingmethod.md)
  An enumeration of rounding methods to use when performing time calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/convertscale(_:method:))*