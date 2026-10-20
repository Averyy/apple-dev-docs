# init(device:delegate:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Creates an object that controls a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init!(device: IOBluetoothDevice!, delegate inDelegate: Any!)
```

```objc
- (instancetype) initWithDevice:(IOBluetoothDevice *) device delegate:(id) inDelegate;
```

## Parameters

- `device`: A remote Bluetooth phone or headset.
- `inDelegate`: A delegate that conforms to the [`IOBluetoothHandsFreeAudioGatewayDelegate`](../iobluetoothhandsfreeaudiogatewaydelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/init(device:delegate:))*