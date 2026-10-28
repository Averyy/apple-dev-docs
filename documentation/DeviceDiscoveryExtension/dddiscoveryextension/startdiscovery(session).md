# startDiscovery(session:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Begins the extension’s device discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
func startDiscovery(session: DDDiscoverySession)
```

## Discussion

The system controls the discovery process using this function by calling it when [`AVRoutePickerView`](../../AVKit/avroutepickerview.md) displays. You code your extension to search the local network or paired Bluetooth devices for a third-party device of interest that you want the system to include in the picker.

## Parameters

- `session`: An object that reports discovery events.

## See Also

### Controlling discovery
- [func stopDiscovery(session: DDDiscoverySession)](./stopdiscovery%28session%29.md)
  Ends the extension’s device discovery process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension/startdiscovery(session:))*