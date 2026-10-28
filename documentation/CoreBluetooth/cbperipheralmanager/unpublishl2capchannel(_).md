# unpublishL2CAPChannel(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) unpublishL2CAPChannel:(CBL2CAPPSM) PSM;
```

## Discussion

After you make this call, the peripheral manager accepts no new connections for this PSM, and closes any existing L2CAP channels using this PSM.

## Parameters

- `PSM`: The Protocol and Service Multiplexer (PSM) to remove from the system.

## See Also

### Using L2CAP Channels
- [func publishL2CAPChannel(withEncryption: Bool)](./publishl2capchannel%28withencryption%29.md)
  Creates a listener for incoming L2CAP channel connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/unpublishl2capchannel(_:))*