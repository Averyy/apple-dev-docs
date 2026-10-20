# addAnnotation(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified annotation to the map view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func addAnnotation(_ annotation: any MKAnnotation)
```

```objc
- (void) addAnnotation:(id<MKAnnotation>) annotation;
```

## Parameters

- `annotation`: The annotation object to add to the receiver. This object must conform to the [`MKAnnotation`](../mkannotation.md) protocol. The map view retains the specified object.

## See Also

### Annotating the map
- [var annotations: [any MKAnnotation]](./annotations.md)
  The annotations associated with the map view.
- [func addAnnotations([any MKAnnotation])](./addannotations%28_%29.md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](./removeannotations%28_%29.md)
  Removes an array of annotation objects from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](./annotations%28in%29.md)
  Returns the annotation objects within the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addannotation(_:))*