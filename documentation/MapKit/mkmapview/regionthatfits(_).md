# regionThatFits(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion
```

```objc
- (MKCoordinateRegion) regionThatFits:(MKCoordinateRegion) region;
```

## Return Value

A region that is still centered on the same point of the map but whose span values are adjusted to fit in the map view’s frame.

## Discussion

You can use this method to normalize the region values before displaying them in the map. This method returns a new region that both contains the specified region and fits neatly inside the map view’s frame.

## Parameters

- `region`: The initial region whose span you want to adjust.

## See Also

### Adjusting map regions and rectangles
- [func mapRectThatFits(MKMapRect) -> MKMapRect](./maprectthatfits%28_%29.md)
  Returns a centered map rectangle with the same aspect ratio as the map view’s frame.
- [func mapRectThatFits(MKMapRect, edgePadding: UIEdgeInsets) -> MKMapRect](./maprectthatfits%28_,edgepadding%29.md)
  Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/regionthatfits(_:))*