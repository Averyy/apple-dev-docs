# DeviceActivityFilter.Devices

**Framework**: DeviceActivity  
**Kind**: struct

A type your app uses to indiciate which devices to include in a device activity report.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Devices
```

#### Overview

Users can control whether a device shares its data with other devices in their circle in iCloud settings.

## Topics

### Initializers
- [init(Set<DeviceActivityData.Device.Model>)](deviceactivityfilter/devices-swift.struct/init(_:).md)
  Filters data for the provided device models.
### Type Properties
- [static let all: DeviceActivityFilter.Devices](deviceactivityfilter/devices-swift.struct/all.md)
  Filters data for all devices that are sharing activity data with the current device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/devices-swift.struct)*