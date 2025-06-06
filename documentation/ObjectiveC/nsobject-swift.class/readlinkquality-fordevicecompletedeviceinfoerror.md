# readLinkQuality(forDeviceComplete:device:info:error:)

**Framework**: Objective-C Runtime  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
func readLinkQuality(forDeviceComplete controller: Any!, device: IOBluetoothDevice!, info: UnsafeMutablePointer<BluetoothHCILinkQualityInfo>!, error: IOReturn)
```

#### Discussion

This delegate gets invoked when an read link quality command complete event occurs. This could occur because you invoked it by issuing a `-readLinkQualityForDevice:` command, or someone else did from another app on the same controller.

## Parameters

- `controller`: Controller object that sent this delegate message.
- `device`: The   device.
- `info`: A pointer to the info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/readlinkquality(fordevicecomplete:device:info:error:))*