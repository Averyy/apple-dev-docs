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

### Operators
- [static func == (DeviceActivityFilter.Devices, DeviceActivityFilter.Devices) -> Bool](deviceactivityfilter/devices-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(Set<DeviceActivityData.Device.Model>)](deviceactivityfilter/devices-swift.struct/init(_:).md)
  Filters data for the provided device models.
### Instance Properties
- [var hashValue: Int](deviceactivityfilter/devices-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivityfilter/devices-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let all: DeviceActivityFilter.Devices](deviceactivityfilter/devices-swift.struct/all.md)
  Filters data for all devices that are sharing activity data with the current device.
### Default Implementations
- [Equatable Implementations](deviceactivityfilter/devices-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/devices-swift.struct)*