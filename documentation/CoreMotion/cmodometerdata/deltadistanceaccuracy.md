# deltaDistanceAccuracy

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The accuracy of the change in distance value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var deltaDistanceAccuracy: CLLocationAccuracy { get }
```

```objc
@property (nonatomic, readonly) CLLocationAccuracy deltaDistanceAccuracy;
```

#### Discussion

This property measures the accuracy of the [`deltaDistance`](./deltadistance.md) property.

## See Also

### Getting the location accuracy
- [var speedAccuracy: CLLocationSpeedAccuracy](./speedaccuracy.md)
  The accuracy of the speed value.
- [var verticalAccuracy: CLLocationAccuracy](./verticalaccuracy.md)
  The validity of the altitude values and their estimated uncertainty, measured in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerdata/deltadistanceaccuracy)*