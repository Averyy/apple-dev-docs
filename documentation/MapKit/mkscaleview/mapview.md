# mapView

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The map view that provides the scale information to the scale view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var mapView: MKMapView? { get set }
```

```objc
@property (nonatomic, weak, nullable) MKMapView * mapView;
```

## See Also

### Getting the scale view attributes
- [var scaleVisibility: MKFeatureVisibility](./scalevisibility.md)
  The visibility of the scale view.
- [var legendAlignment: MKScaleView.Alignment](./legendalignment.md)
  The alignment of the distance information in the scale view.
- [MKScaleView.Alignment](./alignment.md)
  Constants that indicate how the framework should align measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/mapview)*