# setColors:atLocations:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the colors and corresponding unit distance values to create gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (void) setColors:(NSArray<UIColor *> *) colors atLocations:(NSArray<NSNumber *> *) locations;
```

*macOS*

```objc
- (void) setColors:(NSArray<NSColor *> *) colors atLocations:(NSArray<NSNumber *> *) locations;
```

## Discussion

The unit distance value of `0` represents the start of the polyline, and `1` represents the end of the polyline. A gradient may have any number of steps along the length of the polyline.

To determine a location along the polyline, use [`location(atPointIndex:)`](../mkmultipoint/location%28atpointindex%29.md), or retrieve a set of locations using [`locationsAtPointIndexes:`](../mkmultipoint/locationsatpointindexes_.md).

## Parameters

- `colors`: An array of colors making up the transition points of the gradient.
- `locations`: An array of unit distance values that correspond to the provided colors.

## See Also

### Accessing the gradient colors
- [var colors: [UIColor]](./colors.md)
  An array that represents the gradient’s color transition points.
- [locations](./locations-50knt.md)
  An array of location indices corresponding to their respective colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgradientpolylinerenderer/setcolors:atlocations:)*