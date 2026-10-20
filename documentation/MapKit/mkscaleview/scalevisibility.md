# scaleVisibility

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The visibility of the scale view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var scaleVisibility: MKFeatureVisibility { get set }
```

```objc
@property (nonatomic, assign) MKFeatureVisibility scaleVisibility;
```

#### Discussion

You can configure a scale view to be visible all the time or only when the scale of the map changes.

## See Also

### Getting the scale view attributes
- [var mapView: MKMapView?](./mapview.md)
  The map view that provides the scale information to the scale view.
- [var legendAlignment: MKScaleView.Alignment](./legendalignment.md)
  The alignment of the distance information in the scale view.
- [MKScaleView.Alignment](./alignment.md)
  Constants that indicate how the framework should align measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/scalevisibility)*