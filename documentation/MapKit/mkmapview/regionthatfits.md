# regionThatFits(_:)

**Framework**: MapKit  
**Kind**: method

Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.

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
func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion
```

#### Return Value

A region that is still centered on the same point of the map but whose span values are adjusted to fit in the map view’s frame.

#### Discussion

You can use this method to normalize the region values before displaying them in the map. This method returns a new region that both contains the specified region and fits neatly inside the map view’s frame.

## Parameters

- `region`: The initial region whose span you want to adjust.

## See Also

- [func mapRectThatFits(MKMapRect) -> MKMapRect](mkmapview/maprectthatfits(_:).md)
  Returns a centered map rectangle with the same aspect ratio as the map view’s frame.
- [func mapRectThatFits(MKMapRect, edgePadding: UIEdgeInsets) -> MKMapRect](mkmapview/maprectthatfits(_:edgepadding:).md)
  Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/regionthatfits(_:))*