# connect(_:options:)

**Framework**: Core Bluetooth  
**Kind**: method

Establishes a local connection to a peripheral.

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
func connect(_ peripheral: CBPeripheral, options: [String : Any]? = nil)
```

#### Discussion

After successfully establishing a local connection to a peripheral, the central manager object calls the [`centralManager(_:didConnect:)`](cbcentralmanagerdelegate/centralmanager(_:didconnect:).md) method of its delegate object. If the connection attempt fails, the central manager object calls the [`centralManager(_:didFailToConnect:error:)`](cbcentralmanagerdelegate/centralmanager(_:didfailtoconnect:error:).md) method of its delegate object instead. Attempts to connect to a peripheral don’t time out. To explicitly cancel a pending connection to a peripheral, call the [`cancelPeripheralConnection(_:)`](cbcentralmanager/cancelperipheralconnection(_:).md) method. Deallocating `peripheral` also implicitly calls [`cancelPeripheralConnection(_:)`](cbcentralmanager/cancelperipheralconnection(_:).md).

## Parameters

- `peripheral`: The peripheral to which the central is attempting to connect.
- `options`: A dictionary to customize the behavior of the connection. For available options, see  .

## See Also

- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [func cancelPeripheralConnection(CBPeripheral)](cbcentralmanager/cancelperipheralconnection(_:).md)
  Cancels an active or pending local connection to a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/connect(_:options:))*