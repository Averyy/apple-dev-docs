# MKFeatureVisibility

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the visibility of different map features.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MKFeatureVisibility
```

```c
enum MKFeatureVisibility : NSInteger;
```

## Topics

### Visibility options
- [MKFeatureVisibility.adaptive](./mkfeaturevisibility/adaptive.md)
  A constant indicating that the feature adapts to the current map state.
- [MKFeatureVisibility.hidden](./mkfeaturevisibility/hidden.md)
  A constant indicating that the feature is hidden.
- [MKFeatureVisibility.visible](./mkfeaturevisibility/visible.md)
  A constant indicating that the feature is visible.
### Initializers
- [init?(rawValue: Int)](./mkfeaturevisibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the compass attributes
- [var mapView: MKMapView?](./mkcompassbutton/mapview.md)
  The map view that provides the heading information for the compass button.
- [var compassVisibility: MKFeatureVisibility](./mkcompassbutton/compassvisibility.md)
  The visibility of the compass button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkfeaturevisibility)*