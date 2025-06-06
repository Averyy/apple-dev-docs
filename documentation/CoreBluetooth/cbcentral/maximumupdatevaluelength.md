# maximumUpdateValueLength

**Framework**: Core Bluetooth  
**Kind**: property

The maximum amount of data, in bytes, that the central can receive in a single notification or indication.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var maximumUpdateValueLength: Int { get }
```

## Topics

### Related Documentation
- [func updateValue(Data, for: CBMutableCharacteristic, onSubscribedCentrals: [CBCentral]?) -> Bool](cbperipheralmanager/updatevalue(_:for:onsubscribedcentrals:).md)
  Send an updated characteristic value to one or more subscribed centrals, using a notification or indication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentral/maximumupdatevaluelength)*