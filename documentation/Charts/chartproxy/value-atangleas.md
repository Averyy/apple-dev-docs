# value(atAngle:as:)

**Framework**: Swift Charts  
**Kind**: method

Returns the data value at the given angle, or `nil` if the angle does not correspond to a valid data value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func value<P>(atAngle angle: Angle, as: P.Type = P.self) -> P? where P : Plottable
```

#### Return Value

The data value at the given position.

## Parameters

- `angle`: The angle, relative to the plot center, where the 12 o’clock position is interpreted as zero   degrees, increasing clockwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy/value(atangle:as:))*