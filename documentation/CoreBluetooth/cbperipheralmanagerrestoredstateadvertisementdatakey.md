# CBPeripheralManagerRestoredStateAdvertisementDataKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

A dictionary of restored advertising data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBPeripheralManagerRestoredStateAdvertisementDataKey: String
```

```c
extern NSString * const CBPeripheralManagerRestoredStateAdvertisementDataKey;
```

#### Discussion

The value associated with this key is an [`NSDictionary`](../Foundation/nsdictionary.md) that contains the data advertised by the peripheral manager at the time the system quit the app.

## See Also

### State Restoration Dictionary Keys
- [let CBPeripheralManagerRestoredStateServicesKey: String](./cbperipheralmanagerrestoredstateserviceskey.md)
  An array of restored peripheral services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerrestoredstateadvertisementdatakey)*