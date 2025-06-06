# publishL2CAPChannel(withEncryption:)

**Framework**: Core Bluetooth  
**Kind**: method

Creates a listener for incoming L2CAP channel connections.

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
func publishL2CAPChannel(withEncryption encryptionRequired: Bool)
```

#### Discussion

The system determines an unused Protocol and Service Multiplexer (PSM) at the time of publishing, and provides it to your app with [`peripheralManager(_:didPublishL2CAPChannel:error:)`](cbperipheralmanagerdelegate/peripheralmanager(_:didpublishl2capchannel:error:).md). L2CAP channels aren’t discoverable by themselves, so it’s the app’s responsibility to handle PSM discovery on the client.

## Parameters

- `encryptionRequired`:   if the service requires link encryption before a stream can be established.   if the service supports use over an unsecured link.

## See Also

- [func unpublishL2CAPChannel(CBL2CAPPSM)](cbperipheralmanager/unpublishl2capchannel(_:).md)
  Removes a published service from the local system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/publishl2capchannel(withencryption:))*