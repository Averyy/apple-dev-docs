# startDiscovery(session:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method  
**Required**: Yes

Begins the extension’s device discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func startDiscovery(session: DDDiscoverySession)
```

#### Discussion

The system controls the discovery process using this function by calling it when [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) displays. You code your extension to search the local network or paired Bluetooth devices for a third-party device of interest that you want the system to include in the picker.

## Parameters

- `session`: An object that reports discovery events.

## See Also

- [func stopDiscovery(session: DDDiscoverySession)](dddiscoveryextension/stopdiscovery(session:).md)
  Ends the extension’s device discovery process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension/startdiscovery(session:))*