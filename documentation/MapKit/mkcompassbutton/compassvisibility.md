# compassVisibility

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The visibility of the compass button.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var compassVisibility: MKFeatureVisibility { get set }
```

```objc
@property (nonatomic, assign) MKFeatureVisibility compassVisibility;
```

## Discussion

You can configure a compass button to be visible all the time or only when the compass heading changes.

## See Also

### Getting the compass attributes
- [var mapView: MKMapView?](./mapview.md)
  The map view that provides the heading information for the compass button.
- [enum MKFeatureVisibility](../mkfeaturevisibility.md)
  Constants that indicate the visibility of different map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcompassbutton/compassvisibility)*