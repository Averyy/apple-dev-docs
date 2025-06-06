# removeAnnotations(_:)

**Framework**: MapKit  
**Kind**: method

Removes an array of annotation objects from the map view.

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
func removeAnnotations(_ annotations: [any MKAnnotation])
```

#### Discussion

If any annotation object in the array has an associated annotation view, and if that view has a reuse identifier, this method removes the annotation view and queues it internally for later reuse. You can retrieve queued annotation views (and associate them with new annotations) using the [`dequeueReusableAnnotationView(withIdentifier:)`](mkmapview/dequeuereusableannotationview(withidentifier:).md) method.

Removing annotation objects disassociates them from the map view entirely, preventing the map view from displaying them on the map. Typically, you call this method only when you want to hide or delete the specified annotations.

## Parameters

- `annotations`: The array of annotations to remove. Objects in the array need to conform to the   protocol.

## See Also

- [var annotations: [any MKAnnotation]](mkmapview/annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](mkmapview/addannotation(_:).md)
  Adds the specified annotation to the map view.
- [func addAnnotations([any MKAnnotation])](mkmapview/addannotations(_:).md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](mkmapview/removeannotation(_:).md)
  Removes the specified annotation object from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](mkmapview/annotations(in:).md)
  Returns the annotation objects within the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/removeannotations(_:))*