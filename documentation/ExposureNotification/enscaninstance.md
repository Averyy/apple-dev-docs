# ENScanInstance

**Framework**: Exposure Notification  
**Kind**: class

The aggregation of attenuations of beacons received during a scan.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
class ENScanInstance
```

#### Overview

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## Topics

### Getting Scan Instance Properties
- [var minimumAttenuation: ENAttenuation](enscaninstance/minimumattenuation.md)
  The minimum attenuation of beacons received during the scan.
- [var secondsSinceLastScan: Int](enscaninstance/secondssincelastscan.md)
  The number of seconds elapsed since the previous scan.
- [var typicalAttenuation: ENAttenuation](enscaninstance/typicalattenuation.md)
  The aggregation of the attenuations of beacons received during the scan.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Configuring Exposure Notifications](configuring-exposure-notifications.md)
  Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- [class ENExposureConfiguration](enexposureconfiguration.md)
  The object that contains parameters for configuring exposure notification risk scoring behavior.
- [class ENExposureWindow](enexposurewindow.md)
  A set of scan events from observed beacons within a time span.
- [Exposure Parameter Limits](exposure-parameter-limits.md)
  The limits for the parameters you use in exposure risk calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enscaninstance)*