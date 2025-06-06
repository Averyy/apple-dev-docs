# position(forY:)

**Framework**: Swift Charts  
**Kind**: method

Returns the y position for the given data value, or `nil` if the y scale is unavailable or if the data value is invalid. The returned position is relative to the plot.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func position<P>(forY value: P) -> CGFloat? where P : Plottable
```

#### Return Value

The position corresponding to the data value.

## Parameters

- `value`: A data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy/position(fory:))*