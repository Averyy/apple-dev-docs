# peripheralManager(_:willRestoreState:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate the system is about to restore the peripheral manager.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : Any])
```

#### Discussion

For apps that opt in to the state preservation and restoration feature, Core Bluetooth invokes this method when relaunching your app into the background to complete some Bluetooth-related task. Use this method to synchronize the state of your app with the state of the Bluetooth system.

## Parameters

- `peripheral`: The peripheral manager undergoing state restoration.
- `dict`: A dictionary that contains information about the peripheral manager, which the system preserved when the app terminated. For the available keys to this dictionary, see  .

## See Also

- [func peripheralManagerDidUpdateState(CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:).md)
  Tells the delegate the peripheral manager’s state updated.
- [Peripheral Manager State Restoration Options](peripheral-manager-state-restoration-options.md)
  Keys used to specify options when restoring the state of a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:))*