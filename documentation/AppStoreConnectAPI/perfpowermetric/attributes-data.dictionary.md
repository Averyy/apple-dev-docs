# PerfPowerMetric.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Power and Performance Metrics resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object PerfPowerMetric.Attributes
```

## Properties

- `deviceType` (string): A string that represents the device type.
- `metricType` (string): For more information about metric types, see [`MetricCategory`](../metriccategory.md).

  **Allowed Values**: `DISK`, `HANG`, `BATTERY`, `LAUNCH`, `MEMORY`, `ANIMATION`, `TERMINATION`, `STORAGE`
- `platform` (string): **Allowed Values**: `IOS`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/perfpowermetric/attributes-data.dictionary)*