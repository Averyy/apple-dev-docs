# ambientPressure

**Framework**: SensorKit  
**Kind**: property  
**Role**: Type Property

A sensor that provides pressure and temperature metrics.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static let ambientPressure: SRSensor
```

```c
extern SRSensor const SRSensorAmbientPressure;
```

## Discussion

The [`sample`](../srfetchresult/sample.md) type for this sensor is `[`[`CMRecordedPressureData`](../../CoreMotion/cmrecordedpressuredata.md)`]`.

You need to provide a reason to record ambient pressure by adding the [`SRSensorUsageElevation`](../../BundleResources/information-property-list/nssensorkitusagedetail/srsensorusageelevation.md) dictionary to the [`NSSensorKitUsageDetail`](../../BundleResources/information-property-list/nssensorkitusagedetail.md) key in the information property list.

## See Also

### Reading environment sensors
- [static let ambientLightSensor: SRSensor](./ambientlightsensor.md)
  A sensor that provides ambient light information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/ambientpressure)*