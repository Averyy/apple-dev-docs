# mapRectThatFits(_:edgePadding:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect
```

*macOS*

```swift
func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets) -> MKMapRect
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (MKMapRect) mapRectThatFits:(MKMapRect) mapRect edgePadding:(UIEdgeInsets) insets;
```

*macOS*

```objc
- (MKMapRect) mapRectThatFits:(MKMapRect) mapRect edgePadding:(NSEdgeInsets) insets;
```

#### Return Value

MapKit centers the map rectangle on the same point of the map, and adjusts the width and height to fit in the map view’s frame, minus its inset values.

## Parameters

- `mapRect`: The initial map rectangle with the width and height you want to adjust.
- `insets`: The distance (in screen points) by which to inset the returned rectangle from the actual boundaries of the map view’s frame.

## See Also

### Adjusting map regions and rectangles
- [func regionThatFits(MKCoordinateRegion) -> MKCoordinateRegion](./regionthatfits%28_%29.md)
  Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.
- [func mapRectThatFits(MKMapRect) -> MKMapRect](./maprectthatfits%28_%29.md)
  Returns a centered map rectangle with the same aspect ratio as the map view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/maprectthatfits(_:edgepadding:))*