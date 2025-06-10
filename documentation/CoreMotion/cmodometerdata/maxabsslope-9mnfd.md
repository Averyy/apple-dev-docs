# maxAbsSlope

**Framework**: Core Motion  
**Kind**: property

The maximum absolute slope at the location toward all directions, measured in degrees.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var maxAbsSlope: Double? { get }
```

#### Discussion

If the maximum absolute slope is invalid due to low GPS accuracy, this property is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

## See Also

- [var speed: CLLocationSpeed](cmodometerdata/speed.md)
  The instantaneous velocity of the device, measured in meters per second.
- [var slope: Double?](cmodometerdata/slope-9h3m4.md)
  The slope at the location toward the direction of travel, measured in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerdata/maxabsslope-9mnfd)*