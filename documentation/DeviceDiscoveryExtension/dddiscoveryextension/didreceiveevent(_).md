# didReceiveEvent(_:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a device event from the system to the extension.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
func didReceiveEvent(_ event: DDDeviceEvent)
```

#### Discussion

The system calls this function to give the app’s `DDDiscoveryExtension` information about the device. For example, when someone selects the device in the AirPlay menu ([`AVRoutePickerView`](../../AVKit/avroutepickerview.md)), the system notifies the extension of the state change by invoking this callback.

## Parameters

- `event`: A moment of interest in the device discovery life cycle.

## Default Implementations

### DDDiscoveryExtension Implementations
- [func didReceiveEvent(DDDeviceEvent)](./didreceiveevent%28_%29-7usr8.md)
  A default, blank implementation for when the system notifies the extension of a device event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension/didreceiveevent(_:))*