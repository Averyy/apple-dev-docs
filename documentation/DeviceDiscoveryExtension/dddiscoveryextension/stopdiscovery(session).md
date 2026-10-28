# stopDiscovery(session:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Ends the extension’s device discovery process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
func stopDiscovery(session: DDDiscoverySession)
```

## Discussion

The system controls the discovery process using this function by calling it when [`AVRoutePickerView`](../../AVKit/avroutepickerview.md) dismisses. Your extension’s implementation performs any cleanup necessary, such as stopping Bluetooth or Bonjour scanning.

## Parameters

- `session`: An object that reports discovery events.

## See Also

### Controlling discovery
- [func startDiscovery(session: DDDiscoverySession)](./startdiscovery%28session%29.md)
  Begins the extension’s device discovery process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension/stopdiscovery(session:))*