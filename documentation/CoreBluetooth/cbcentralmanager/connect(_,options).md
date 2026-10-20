# connect(_:options:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) connectPeripheral:(CBPeripheral *) peripheral options:(NSDictionary<NSString *,id> *) options;
```

#### Discussion

After successfully establishing a local connection to a peripheral, the central manager object calls the [`centralManager(_:didConnect:)`](../cbcentralmanagerdelegate/centralmanager%28_,didconnect%29.md) method of its delegate object. If the connection attempt fails, the central manager object calls the [`centralManager(_:didFailToConnect:error:)`](../cbcentralmanagerdelegate/centralmanager%28_,didfailtoconnect,error%29.md) method of its delegate object instead. Attempts to connect to a peripheral don’t time out. To explicitly cancel a pending connection to a peripheral, call the [`cancelPeripheralConnection(_:)`](./cancelperipheralconnection%28_%29.md) method. Deallocating `peripheral` also implicitly calls [`cancelPeripheralConnection(_:)`](./cancelperipheralconnection%28_%29.md).

## Parameters

- `peripheral`: The peripheral to which the central is attempting to connect.
- `options`: A dictionary to customize the behavior of the connection. For available options, see [Peripheral Connection Options](../peripheral-connection-options.md).

## See Also

### Establishing or Canceling Connections with Peripherals
- [Peripheral Connection Options](../peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [func cancelPeripheralConnection(CBPeripheral)](./cancelperipheralconnection%28_%29.md)
  Cancels an active or pending local connection to a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/connect(_:options:))*