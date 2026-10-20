# setColors(_:locations:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the macOS colors and corresponding unit distance values to create gradients.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func setColors(_ colors: [NSColor], locations: [CGFloat])
```

#### Discussion

The unit distance value of `0` represents the start of the polyline, and `1` represents the end of the polyline. A gradient may have any number of steps along the length of the polyline.

To determine a location along the polyline, use [`location(atPointIndex:)`](../mkmultipoint/location%28atpointindex%29.md), or retrieve a set of locations using [`locations`](./locations-7k6qz.md).

## Parameters

- `colors`: An array of colors making up the transition points of the gradient.
- `locations`: An array of unit distance values that correspond to the provided colors.

## See Also

### Accessing the gradient colors
- [func setColors([UIColor], locations: [CGFloat])](./setcolors%28_,locations%29-3xrou.md)
  Sets the iOS colors and corresponding unit distance values to create gradients.
- [var colors: [UIColor]](./colors.md)
  An array that represents the gradient’s color transition points.
- [var locations: [CGFloat]](./locations-7k6qz.md)
  An array of location indexes that correspond to their respective colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/setcolors(_:locations:)-1tuft)*