# peripheral(_:didCompleteChannelSoundingSession:)

**Framework**: Core Bluetooth  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
optional func peripheral(_ peripheral: CBPeripheral, didCompleteChannelSoundingSession error: (any Error)?)
```

#### Discussion

This method is called when a channel sounding session completes.

## Parameters

- `peripheral`: The peripheral providing this update.
- `error`: If an error occurred, the cause of the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didcompletechannelsoundingsession:))*