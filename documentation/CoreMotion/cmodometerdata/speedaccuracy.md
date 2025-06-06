# speedAccuracy

**Framework**: Core Motion  
**Kind**: property

The accuracy of the speed value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var speedAccuracy: CLLocationSpeedAccuracy { get }
```

#### Discussion

This property measures the accuracy of the [`speed`](cmodometerdata/speed.md) property. When this property contains `0` or a positive number, the value in the `speed` property is plus or minus the specified number of meters per second. When this property contains a negative number, the value in the `speed` property is invalid.

## See Also

- [var verticalAccuracy: CLLocationAccuracy](cmodometerdata/verticalaccuracy.md)
  The validity of the altitude values and their estimated uncertainty, measured in meters.
- [var deltaDistanceAccuracy: CLLocationAccuracy](cmodometerdata/deltadistanceaccuracy.md)
  The accuracy of the change in distance value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerdata/speedaccuracy)*