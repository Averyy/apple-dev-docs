# isSupported(_:)

**Framework**: DeviceDiscoveryUI  
**Kind**: method

Returns a Boolean value that indicates whether the current device supports device discovery using Wi-FI Aware.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency static func isSupported(_ listenerProvider: any ListenerProvider) -> Bool
```

## Parameters

- `listenerProvider`: A doc://com.apple.documentation/documentaiton/network/ListenerProvider protocol object that defines the service the listener advertises.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingviewcontroller/issupported(_:))*