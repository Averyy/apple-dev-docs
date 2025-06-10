# scaleVisibility

**Framework**: MapKit  
**Kind**: property

The visibility of the scale view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scaleVisibility: MKFeatureVisibility { get set }
```

#### Discussion

You can configure a scale view to be visible all the time or only when the scale of the map changes.

## See Also

- [var mapView: MKMapView?](mkscaleview/mapview.md)
  The map view that provides the scale information to the scale view.
- [var legendAlignment: MKScaleView.Alignment](mkscaleview/legendalignment.md)
  The alignment of the distance information in the scale view.
- [MKScaleView.Alignment](mkscaleview/alignment.md)
  Constants that indicate how the framework should align measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/scalevisibility)*