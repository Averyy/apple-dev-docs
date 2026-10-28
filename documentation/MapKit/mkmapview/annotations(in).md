# annotations(in:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func annotations(in mapRect: MKMapRect) -> Set<AnyHashable>
```

```objc
- (NSSet<id<MKAnnotation>> *) annotationsInMapRect:(MKMapRect) mapRect;
```

## Return Value

The set of annotation objects within `mapRect`.

## Discussion

This method offers a fast way to retrieve the annotation objects in a particular portion of the map. It’s much faster than doing a linear search of the objects in the [`annotations`](./annotations.md) property yourself.

## Parameters

- `mapRect`: The portion of the map that you want to search for annotations.

## See Also

### Annotating the map
- [var annotations: [any MKAnnotation]](./annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](./addannotation%28_%29.md)
  Adds the specified annotation to the map view.
- [func addAnnotations([any MKAnnotation])](./addannotations%28_%29.md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](./removeannotation%28_%29.md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](./removeannotations%28_%29.md)
  Removes an array of annotation objects from the map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/annotations(in:))*