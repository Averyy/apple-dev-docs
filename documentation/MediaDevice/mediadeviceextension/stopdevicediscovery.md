# stopDeviceDiscovery()

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when the user dismisses the UI element that is showing devices.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
func stopDeviceDiscovery()
```

#### Discussion

Stop any active network discovery operations started in [`startDeviceDiscovery()`](mediadeviceextension/startdevicediscovery().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/stopdevicediscovery())*