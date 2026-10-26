# MKGradientPolylineRenderer

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A visual representation of any polyline overlay object with a gradient.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MKGradientPolylineRenderer
```

```objc
@interface MKGradientPolylineRenderer : MKPolylineRenderer
```

#### Overview

This renderer only applies a stroke to the line; it doesn’t fill it. Set the gradients with [`setColors:atLocations:`](./mkgradientpolylinerenderer/setcolors_atlocations_.md) and pair colors to locations that MapKit represents as unit distance values along the distance of the polyline. Don’t subclass `MKGradientPolylineRenderer`. Use the class as-is.

The gradient displays itself along the direction of the line.

## Topics

### Accessing the gradient colors
- [func setColors([UIColor], locations: [CGFloat])](./mkgradientpolylinerenderer/setcolors%28_,locations%29-3xrou.md)
  Sets the iOS colors and corresponding unit distance values to create gradients.
- [func setColors([NSColor], locations: [CGFloat])](./mkgradientpolylinerenderer/setcolors%28_,locations%29-1tuft.md)
  Sets the macOS colors and corresponding unit distance values to create gradients.
- [var colors: [UIColor]](./mkgradientpolylinerenderer/colors.md)
  An array that represents the gradient’s color transition points.
- [var locations: [CGFloat]](./mkgradientpolylinerenderer/locations-7k6qz.md)
  An array of location indexes that correspond to their respective colors.
- [- setColors:atLocations:](./mkgradientpolylinerenderer/setcolors_atlocations_.md)
  Sets the colors and corresponding unit distance values to create gradients.
- [locations](./mkgradientpolylinerenderer/locations-50knt.md)
  An array of location indices corresponding to their respective colors.

## Relationships

### Inherits From
- [MKPolylineRenderer](./mkpolylinerenderer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Multiple segment lines
- [class MKPolyline](./mkpolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [class MKGeodesicPolyline](./mkgeodesicpolyline.md)
  An open polygon overlay consisting of line segments that follow the contours of the Earth to create the shortest path between the specified points.
- [class MKMultiPolyline](./mkmultipolyline.md)
  A collection of multipolyline shapes, each consisting of one or more connected line segments.
- [class MKPolylineRenderer](./mkpolylinerenderer.md)
  A visual representation of any polyline overlay object.
- [class MKMultiPolylineRenderer](./mkmultipolylinerenderer.md)
  A visual representation of multiple polyline overlay objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer)*