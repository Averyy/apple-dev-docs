# publishL2CAPChannel(withEncryption:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) publishL2CAPChannelWithEncryption:(BOOL) encryptionRequired;
```

## Discussion

The system determines an unused Protocol and Service Multiplexer (PSM) at the time of publishing, and provides it to your app with [`peripheralManager(_:didPublishL2CAPChannel:error:)`](../cbperipheralmanagerdelegate/peripheralmanager%28_,didpublishl2capchannel,error%29.md). L2CAP channels aren’t discoverable by themselves, so it’s the app’s responsibility to handle PSM discovery on the client.

## Parameters

- `encryptionRequired`: [`true`](../../Swift/true.md) if the service requires link encryption before a stream can be established. [`false`](../../Swift/false.md) if the service supports use over an unsecured link.

## See Also

### Using L2CAP Channels
- [func unpublishL2CAPChannel(CBL2CAPPSM)](./unpublishl2capchannel%28_%29.md)
  Removes a published service from the local system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/publishl2capchannel(withencryption:))*