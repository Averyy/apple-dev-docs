# CGLineCap.square

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case square
```

```c
kCGLineCapSquare
```

## See Also

### Constants
- [CGLineCap.butt](./butt.md)
  A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.
- [CGLineCap.round](./round.md)
  A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglinecap/square)*