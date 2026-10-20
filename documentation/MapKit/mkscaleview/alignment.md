# MKScaleView.Alignment

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how the framework should align measurements.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Alignment
```

```c
enum MKScaleViewAlignment : NSInteger;
```

## Topics

### Alignment options
- [MKScaleView.Alignment.leading](./alignment/leading.md)
  Scale measurements begin at the leading edge of the view.
- [MKScaleView.Alignment.trailing](./alignment/trailing.md)
  Scale measurements begin at the trailing edge of the view.
- [MKScaleView.Alignment.center](./alignment/center.md)
  Scale measurements appear horizontally centered within the view.
### Initializers
- [init?(rawValue: Int)](./alignment/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the scale view attributes
- [var mapView: MKMapView?](./mapview.md)
  The map view that provides the scale information to the scale view.
- [var scaleVisibility: MKFeatureVisibility](./scalevisibility.md)
  The visibility of the scale view.
- [var legendAlignment: MKScaleView.Alignment](./legendalignment.md)
  The alignment of the distance information in the scale view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/alignment)*