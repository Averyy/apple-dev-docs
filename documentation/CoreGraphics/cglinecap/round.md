# CGLineCap.round

**Framework**: Core Graphics  
**Kind**: case

A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case round
```

## See Also

- [CGLineCap.butt](cglinecap/butt.md)
  A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.
- [CGLineCap.square](cglinecap/square.md)
  A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinecap/round)*