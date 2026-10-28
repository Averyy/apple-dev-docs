# annotations

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The annotations associated with the map view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var annotations: [any MKAnnotation] { get }
```

```objc
@property (nonatomic, readonly) NSArray<id<MKAnnotation>> * annotations;
```

## Discussion

The objects in this array adopt the [`MKAnnotation`](../mkannotation.md) protocol. If the map view has no associated annotations, the value of this property is an empty array.

## See Also

### Annotating the map
- [func addAnnotation(any MKAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation to the map view.
- [func addAnnotations([any MKAnnotation])](./addannotations%28_%29.md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](./removeannotations%28_%29.md)
  Removes an array of annotation objects from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](./annotations%28in%29.md)
  Returns the annotation objects within the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/annotations)*