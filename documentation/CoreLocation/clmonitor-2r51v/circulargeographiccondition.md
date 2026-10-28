# CLMonitor.CircularGeographicCondition

**Framework**: Core Location  
**Kind**: struct  
**Role**: Structure

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

## Overview

Use `CLMonitor.CircularGeographicCondition` to monitor events that occur in a circular geographic condition that you describe.

## Topics

### Creating a circular geographic condition
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](./circulargeographiccondition/init%28center,radius%29.md)
  Creates a circular geographic condition with a center point and radius you specify.
### Condition characteristics
- [let center: CLLocationCoordinate2D](./circulargeographiccondition/center.md)
  The center point of the condition’s area.
- [let radius: CLLocationDistance](./circulargeographiccondition/radius.md)
  The radius of the condition’s area, in meters.

## Relationships

### Conforms To
- [CLCondition](../clcondition-swift.protocol.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitor conditions
- [CLMonitor.BeaconIdentityCondition](./beaconidentitycondition.md)
  A condition that describes the characteristics of a beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/circulargeographiccondition)*