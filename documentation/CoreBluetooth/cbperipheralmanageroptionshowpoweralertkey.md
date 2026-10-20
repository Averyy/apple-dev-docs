# CBPeripheralManagerOptionShowPowerAlertKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.

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
let CBPeripheralManagerOptionShowPowerAlertKey: String
```

```c
extern NSString * const CBPeripheralManagerOptionShowPowerAlertKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../Foundation/nsnumber.md). If the key isn’t specified, the default value is [`false`](../Swift/false.md).

## See Also

### Initialization Options
- [let CBPeripheralManagerOptionRestoreIdentifierKey: String](./cbperipheralmanageroptionrestoreidentifierkey.md)
  A string containing a unique identifier (UID) for the peripheral manager to instantiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionshowpoweralertkey)*