# addAnnotations(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func addAnnotations(_ annotations: [any MKAnnotation])
```

```objc
- (void) addAnnotations:(NSArray<id<MKAnnotation>> *) annotations;
```

## Parameters

- `annotations`: An array of annotation objects. Each object in the array must conform to the [`MKAnnotation`](../mkannotation.md) protocol. The map view retains the individual annotation objects.

## See Also

### Annotating the map
- [var annotations: [any MKAnnotation]](./annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation to the map view.
- [func removeAnnotation(any MKAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](./removeannotations%28_%29.md)
  Removes an array of annotation objects from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](./annotations%28in%29.md)
  Returns the annotation objects within the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addannotations(_:))*