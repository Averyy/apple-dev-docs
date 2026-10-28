# slope

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The slope at the location toward the direction of travel, measured in degrees.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var slope: Double? { get }
```

## Discussion

If the slope measurement is invalid, this property is [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Getting speed and slope
- [var speed: CLLocationSpeed](./speed.md)
  The instantaneous velocity of the device, measured in meters per second.
- [var maxAbsSlope: Double?](./maxabsslope-9mnfd.md)
  The maximum absolute slope at the location toward all directions, measured in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerdata/slope-9h3m4)*