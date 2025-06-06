# centralManager(_:willRestoreState:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate the system is about to restore the central manager, as part of relaunching the app into the background.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : Any])
```

#### Discussion

This method only applies to apps that opt in to the state preservation and restoration feature of Core Bluetooth. The system invokes this method when relaunching your app into the background to complete some Bluetooth-related task. Use this method to synchronize the state of your app with the state of the Bluetooth system.

## Parameters

- `central`: The central manager that provides this information.
- `dict`: A dictionary that contains information about the central manager preserved by the system when it terminated the app. For the available keys to this dictionary, see  .

## See Also

- [func centralManagerDidUpdateState(CBCentralManager)](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md)
  Tells the delegate the central manager’s state updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:willrestorestate:))*