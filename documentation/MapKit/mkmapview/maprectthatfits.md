# mapRectThatFits(_:)

**Framework**: MapKit  
**Kind**: method

Returns a centered map rectangle with the same aspect ratio as the map view’s frame.

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
func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect
```

#### Return Value

MapKit centers the map rectangle on the same point of the map, and adjusts the width and height to fit in the map view’s frame.

#### Discussion

Returns a map rectangle with the same aspect ratio as the map view’s frame, centered at the same location as the specified map rectangle.

You can use this method to normalize map rectangle values before displaying the corresponding area. This method returns a new map rectangle that both contains the specified rectangle and fits neatly inside the map view’s frame.

## Parameters

- `mapRect`: The initial map rectangle whose width and height you want to adjust to the view frame.

## See Also

- [func regionThatFits(MKCoordinateRegion) -> MKCoordinateRegion](mkmapview/regionthatfits(_:).md)
  Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.
- [func mapRectThatFits(MKMapRect, edgePadding: UIEdgeInsets) -> MKMapRect](mkmapview/maprectthatfits(_:edgepadding:).md)
  Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/maprectthatfits(_:))*