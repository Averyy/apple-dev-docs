# annotations(in:)

**Framework**: MapKit  
**Kind**: method

Returns the annotation objects within the specified map rectangle.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func annotations(in mapRect: MKMapRect) -> Set<AnyHashable>
```

#### Return Value

The set of annotation objects within `mapRect`.

#### Discussion

This method offers a fast way to retrieve the annotation objects in a particular portion of the map. It’s much faster than doing a linear search of the objects in the [`annotations`](mkmapview/annotations.md) property yourself.

## Parameters

- `mapRect`: The portion of the map that you want to search for annotations.

## See Also

- [var annotations: [any MKAnnotation]](mkmapview/annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](mkmapview/addannotation(_:).md)
  Adds the specified annotation to the map view.
- [func addAnnotations([any MKAnnotation])](mkmapview/addannotations(_:).md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](mkmapview/removeannotation(_:).md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](mkmapview/removeannotations(_:).md)
  Removes an array of annotation objects from the map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/annotations(in:))*