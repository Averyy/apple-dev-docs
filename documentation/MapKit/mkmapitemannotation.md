# MKMapItemAnnotation

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

An annotation that represents a map item

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MKMapItemAnnotation
```

```objc
@interface MKMapItemAnnotation : NSObject
```

## Mentions

- [Identifying unique locations with Place IDs](./identifying-unique-locations-with-place-ids.md)

## Topics

### Creating a map item annotation
- [init?(mapItem: MKMapItem)](./mkmapitemannotation/init%28mapitem%29.md)
  Creates a map item annotation
### Accessing the annotation’s map item
- [var mapItem: MKMapItem](./mkmapitemannotation/mapitem.md)
  The map item represented by this annotation

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MKAnnotation](./mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Location annotations
- [Annotating a Map with Custom Data](./annotating-a-map-with-custom-data.md)
  Annotate a map with location-specific data using default and customized annotation views and callouts.
- [class MKPointAnnotation](./mkpointannotation.md)
  A string-based piece of location-specific data that you apply to a specific point on a map.
- [class MKMarkerAnnotationView](./mkmarkerannotationview.md)
  An annotation view that displays a balloon-shaped marker at the designated location.
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemannotation)*