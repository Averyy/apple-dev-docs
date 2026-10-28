# DeviceActivityFilter.Devices

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

A type your app uses to indiciate which devices to include in a device activity report.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Devices
```

## Overview

Users can control whether a device shares its data with other devices in their circle in iCloud settings.

## Topics

### Initializers
- [init(Set<DeviceActivityData.Device.Model>)](./devices-swift.struct/init%28_%29.md)
  Filters data for the provided device models.
### Type Properties
- [static let all: DeviceActivityFilter.Devices](./devices-swift.struct/all.md)
  Filters data for all devices that are sharing activity data with the current device.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/devices-swift.struct)*