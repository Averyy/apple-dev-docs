# CBPeripheralManagerRestoredStateServicesKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

An array of restored peripheral services.

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
let CBPeripheralManagerRestoredStateServicesKey: String
```

```c
extern NSString * const CBPeripheralManagerRestoredStateServicesKey;
```

## Discussion

The value associated with this key is an [`NSArray`](../Foundation/nsarray.md) of [`CBMutableService`](./cbmutableservice.md) objects. It contains all of the services that previously published to the local peripheral’s database when the system quit the app.

Restoration includes all information about a service, including any included services, characteristics, characteristic descriptors, and subscribed centrals.

## See Also

### State Restoration Dictionary Keys
- [let CBPeripheralManagerRestoredStateAdvertisementDataKey: String](./cbperipheralmanagerrestoredstateadvertisementdatakey.md)
  A dictionary of restored advertising data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerrestoredstateserviceskey)*