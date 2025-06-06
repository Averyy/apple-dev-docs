# peripheral(_:didOpen:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Delivers the result of an attempt to open an L2CAP channel.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func peripheral(_ peripheral: CBPeripheral, didOpen channel: CBL2CAPChannel?, error: (any Error)?)
```

#### Discussion

This method delivers the result of a previous call to [`openL2CAPChannel(_:)`](cbperipheral/openl2capchannel(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:didopen:error:))*