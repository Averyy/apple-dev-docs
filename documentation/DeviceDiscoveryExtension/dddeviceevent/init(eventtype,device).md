# init(eventType:device:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: init

Creates an event object that conveys status for a discovered device of interest.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
init(eventType type: DDDeviceEvent.EventType, device: DDDevice)
```

## Parameters

- `type`: The option that represents the device’s status in the device discovery life cycle.
- `device`: The discovered device of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent/init(eventtype:device:))*