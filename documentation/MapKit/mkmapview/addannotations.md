# addAnnotations(_:)

**Framework**: MapKit  
**Kind**: method

Adds an array of annotation objects to the map view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAnnotations(_ annotations: [any MKAnnotation])
```

## Parameters

- `annotations`: An array of annotation objects. Each object in the array must conform to the   protocol. The map view retains the individual annotation objects.

## See Also

- [var annotations: [any MKAnnotation]](mkmapview/annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](mkmapview/addannotation(_:).md)
  Adds the specified annotation to the map view.
- [func removeAnnotation(any MKAnnotation)](mkmapview/removeannotation(_:).md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](mkmapview/removeannotations(_:).md)
  Removes an array of annotation objects from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](mkmapview/annotations(in:).md)
  Returns the annotation objects within the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addannotations(_:))*