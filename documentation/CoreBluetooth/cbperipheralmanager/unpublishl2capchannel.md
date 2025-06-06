# unpublishL2CAPChannel(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Removes a published service from the local system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func unpublishL2CAPChannel(_ PSM: CBL2CAPPSM)
```

#### Discussion

After you make this call, the peripheral manager accepts no new connections for this PSM, and closes any existing L2CAP channels using this PSM.

## Parameters

- `PSM`: The Protocol and Service Multiplexer (PSM) to remove from the system.

## See Also

- [func publishL2CAPChannel(withEncryption: Bool)](cbperipheralmanager/publishl2capchannel(withencryption:).md)
  Creates a listener for incoming L2CAP channel connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/unpublishl2capchannel(_:))*