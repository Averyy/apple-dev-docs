# CLMonitor.CircularGeographicCondition

**Framework**: Core Location  
**Kind**: struct

A condition that describes a circular geographic area that a center point and radius define.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct CircularGeographicCondition
```

#### Overview

Use `CLMonitor.CircularGeographicCondition` to monitor events that occur in a circular geographic condition that you describe.

## Topics

### Creating a circular geographic condition
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](clmonitor-2r51v/circulargeographiccondition/init(center:radius:).md)
  Creates a circular geographic condition with a center point and radius you specify.
### Condition characteristics
- [let center: CLLocationCoordinate2D](clmonitor-2r51v/circulargeographiccondition/center.md)
  The center point of the condition’s area.
- [let radius: CLLocationDistance](clmonitor-2r51v/circulargeographiccondition/radius.md)
  The radius of the condition’s area, in meters.

## Relationships

### Conforms To
- [CLCondition](clcondition-swift.protocol.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CLMonitor.BeaconIdentityCondition](clmonitor-2r51v/beaconidentitycondition.md)
  A condition that describes the characteristics of a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/circulargeographiccondition)*