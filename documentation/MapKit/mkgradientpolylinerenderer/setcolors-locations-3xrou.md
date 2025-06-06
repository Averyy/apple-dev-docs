# setColors(_:locations:)

**Framework**: MapKit  
**Kind**: method

Sets the iOS colors and corresponding unit distance values to create gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func setColors(_ colors: [UIColor], locations: [CGFloat])
```

#### Discussion

The unit distance value of `0` represents the start of the polyline, and `1` represents the end of the polyline. A gradient may have any number of steps along the length of the polyline.

To determine a location along the polyline, use [`location(atPointIndex:)`](mkmultipoint/location(atpointindex:).md), or retrieve a set of locations using [`locations`](mkgradientpolylinerenderer/locations-7k6qz.md).

## Parameters

- `colors`: An array of colors making up the transition points of the gradient.
- `locations`: An array of unit distance values that correspond to the provided colors.

## See Also

- [func setColors([NSColor], locations: [CGFloat])](mkgradientpolylinerenderer/setcolors(_:locations:)-1tuft.md)
  Sets the macOS colors and corresponding unit distance values to create gradients.
- [var colors: [UIColor]](mkgradientpolylinerenderer/colors.md)
  An array that represents the gradient’s color transition points.
- [var locations: [CGFloat]](mkgradientpolylinerenderer/locations-7k6qz.md)
  An array of location indexes that correspond to their respective colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/setcolors(_:locations:)-3xrou)*