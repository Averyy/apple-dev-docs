# legendAlignment

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the distance information in the scale view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var legendAlignment: MKScaleView.Alignment { get set }
```

```objc
@property (nonatomic, assign) MKScaleViewAlignment legendAlignment;
```

#### Discussion

This property determines whether measurements start at the leading or trailing edge of the view. The default value of this property is [`MKScaleView.Alignment.leading`](./alignment/leading.md).

## See Also

### Getting the scale view attributes
- [var mapView: MKMapView?](./mapview.md)
  The map view that provides the scale information to the scale view.
- [var scaleVisibility: MKFeatureVisibility](./scalevisibility.md)
  The visibility of the scale view.
- [MKScaleView.Alignment](./alignment.md)
  Constants that indicate how the framework should align measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/legendalignment)*