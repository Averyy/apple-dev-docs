# stopDiscovery(session:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method  
**Required**: Yes

Ends the extension’s device discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func stopDiscovery(session: DDDiscoverySession)
```

#### Discussion

The system controls the discovery process using this function by calling it when [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) dismisses. Your extension’s implementation performs any cleanup necessary, such as stopping Bluetooth or Bonjour scanning.

## Parameters

- `session`: An object that reports discovery events.

## See Also

- [func startDiscovery(session: DDDiscoverySession)](dddiscoveryextension/startdiscovery(session:).md)
  Begins the extension’s device discovery process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension/stopdiscovery(session:))*