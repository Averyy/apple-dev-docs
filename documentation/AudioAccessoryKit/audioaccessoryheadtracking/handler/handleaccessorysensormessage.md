# handleAccessorySensorMessage(_:)

**Framework**: AudioAccessoryKit  
**Kind**: method  
**Required**: Yes

Called when a `TransportMessage` arrives from the accessory’s transport extension on the inbound channel.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func handleAccessorySensorMessage(_ message: TransportMessage)
```

#### Discussion

Use this to receive control-plane payloads from your `AccessoryTransportExtension` (e.g. configuration acknowledgements, vendor-specific messages). For raw IMU sample delivery, the extension should call `Session.sendDataToAudioExtension(_:)` directly.

## Parameters

- `message`: The transport-layer message as delivered by `DeviceAccess`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/handler/handleaccessorysensormessage(_:))*