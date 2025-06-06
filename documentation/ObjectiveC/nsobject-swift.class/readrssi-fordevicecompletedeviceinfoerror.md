# readRSSI(forDeviceComplete:device:info:error:)

**Framework**: Objective-C Runtime  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
func readRSSI(forDeviceComplete controller: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCIRSSIInfo>!, error: IOReturn)
```

#### Discussion

This delegate gets invoked when an RSSI command complete event occurs. This could occur because you invoked it by issuing a `-readRSSIForDevice:` command, or someone else did from another app on the same controller.

## Parameters

- `controller`: Controller object that sent this delegate message.
- `device`: The   device.
- `info`: A pointer to the info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/readrssi(fordevicecomplete:device:info:error:))*