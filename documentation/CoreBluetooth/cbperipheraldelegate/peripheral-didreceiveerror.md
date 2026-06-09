# peripheral(_:didReceive:error:)

**Framework**: Core Bluetooth  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
optional func peripheral(_ peripheral: CBPeripheral, didReceive results: CBChannelSoundingProcedureResults?, error: (any Error)?)
```

#### Discussion

This method returns the results of a channel sounding procedure.

## Parameters

- `peripheral`: The peripheral providing this update.
- `results`: An object containing the results of a channel sounding procedure.
- `error`: If an error occurred, the cause of the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didreceive:error:))*