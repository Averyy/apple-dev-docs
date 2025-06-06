# cancelPeripheralConnection(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Cancels an active or pending local connection to a peripheral.

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
func cancelPeripheralConnection(_ peripheral: CBPeripheral)
```

#### Discussion

This method is nonblocking, and any [`CBPeripheral`](cbperipheral.md) class commands that are still pending to `peripheral` may not complete. Because other apps may still have a connection to the peripheral, canceling a local connection doesn’t guarantee that the underlying physical link is immediately disconnected. From the app’s perspective, however, the peripheral is effectively disconnected, and the central manager object calls the [`centralManager(_:didDisconnectPeripheral:error:)`](cbcentralmanagerdelegate/centralmanager(_:diddisconnectperipheral:error:).md) method of its delegate object.

## Parameters

- `peripheral`: The peripheral to which the central manager is either trying to connect or has already connected.

## See Also

- [func connect(CBPeripheral, options: [String : Any]?)](cbcentralmanager/connect(_:options:).md)
  Establishes a local connection to a peripheral.
- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/cancelperipheralconnection(_:))*