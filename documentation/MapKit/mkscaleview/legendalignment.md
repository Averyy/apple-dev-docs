# legendAlignment

**Framework**: MapKit  
**Kind**: property

The alignment of the distance information in the scale view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var legendAlignment: MKScaleView.Alignment { get set }
```

#### Discussion

This property determines whether measurements start at the leading or trailing edge of the view. The default value of this property is [`MKScaleView.Alignment.leading`](mkscaleview/alignment/leading.md).

## See Also

- [var mapView: MKMapView?](mkscaleview/mapview.md)
  The map view that provides the scale information to the scale view.
- [var scaleVisibility: MKFeatureVisibility](mkscaleview/scalevisibility.md)
  The visibility of the scale view.
- [MKScaleView.Alignment](mkscaleview/alignment.md)
  Constants that indicate how the framework should align measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/legendalignment)*