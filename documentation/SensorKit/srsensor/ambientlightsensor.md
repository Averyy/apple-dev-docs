# ambientLightSensor

**Framework**: SensorKit  
**Kind**: property

A sensor that provides ambient light information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static let ambientLightSensor: SRSensor
```

#### Discussion

The [`sample`](srfetchresult/sample.md) type for this sensor is [`SRAmbientLightSample`](srambientlightsample.md).

You need to provide a reason to record ambient light by adding the [`SRSensorUsageAmbientLightSensor`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail/srsensorusageambientlightsensor) dictionary to the [`NSSensorKitUsageDetail`](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedetail) key in the information property list.

## See Also

- [static let ambientPressure: SRSensor](srsensor/ambientpressure.md)
  A sensor that provides pressure and temperature metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/ambientlightsensor)*