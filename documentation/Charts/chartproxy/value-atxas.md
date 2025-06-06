# value(atX:as:)

**Framework**: Swift Charts  
**Kind**: method

Returns the data value at the given x position, or `nil` if the position does not correspond to a valid X value.

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
func value<P>(atX position: CGFloat, as: P.Type = P.self) -> P? where P : Plottable
```

#### Return Value

The data value at the given position.

## Parameters

- `position`: The position at which to obtain the x data value. It should be relative to the plot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy/value(atx:as:))*