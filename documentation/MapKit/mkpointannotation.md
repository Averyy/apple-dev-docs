# MKPointAnnotation

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A string-based piece of location-specific data that you apply to a specific point on a map.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class MKPointAnnotation
```

```objc
@interface MKPointAnnotation : MKShape
```

## Overview

You use this class, rather than define a custom annotation object, in situations where all you want to do is display a title string at the specified point on the map.

## Topics

### Creating a Point Annotation
- [init()](./mkpointannotation/init%28%29.md)
  Creates a map annotation that shows a title string at a point on a map.
- [convenience init(coordinate: CLLocationCoordinate2D)](./mkpointannotation/init%28coordinate%29.md)
  Creates a point annotation at the specified coordinate on the map.
- [convenience init(coordinate: CLLocationCoordinate2D, title: String?, subtitle: String?)](./mkpointannotation/init%28coordinate,title,subtitle%29.md)
  Creates a point annotation displaying a title and subtitle string at the specified coordinate on the map.
### Accessing the Annotation’s Location
- [var coordinate: CLLocationCoordinate2D](./mkpointannotation/coordinate.md)
  The coordinate point of the annotation.

## Relationships

### Inherits From
- [MKShape](./mkshape.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [MKAnnotation](./mkannotation.md)
- [MKGeoJSONObject](./mkgeojsonobject.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Location annotations
- [Annotating a Map with Custom Data](./annotating-a-map-with-custom-data.md)
  Annotate a map with location-specific data using default and customized annotation views and callouts.
- [class MKMapItemAnnotation](./mkmapitemannotation.md)
  An annotation that represents a map item
- [class MKMarkerAnnotationView](./mkmarkerannotationview.md)
  An annotation view that displays a balloon-shaped marker at the designated location.
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointannotation)*