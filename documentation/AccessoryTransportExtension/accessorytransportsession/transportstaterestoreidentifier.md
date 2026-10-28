# transportStateRestoreIdentifier

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Instance Property

An optional identifier for restoring transport state across sessions.

**Availability**:
- iOS 26.5+

## Declaration

```swift
var transportStateRestoreIdentifier: String?
```

## Discussion

Use this identifier to restore an interrupted Bluetooth session in your transport extension. Restoring the prior session allows your extension to skip accessory scanning and notification-forwarding subscription after the system relaunches or resumes your extension from the background. When reinitializing your extension’s [`CBCentralManager`](../../CoreBluetooth/cbcentralmanager.md), pass the value of this property as the `CBCentralManagerOptionRestoreIdentifierKey` options key to the [`init(delegate:queue:options:)`](../../CoreBluetooth/cbcentralmanager/init%28delegate,queue,options%29.md) initializer:

```swift
// Build the options dictionary.
var options: [String: Any] = [:]
if let restoreID = transportSession.transportStateRestoreIdentifier {
    options[CBCentralManagerOptionRestoreIdentifierKey] = restoreID
}

// Instantiate the `CBCentralManager`.
let centralManager = CBCentralManager(
    delegate: self,
    queue: .main,        // Or, use a dedicated dispatch queue.
    options: options
)
```

Create only one `CBCentralManager` with this identifier in your extension. Your extension also needs to implement the [`centralManager(_:willRestoreState:)`](../../CoreBluetooth/cbcentralmanagerdelegate/centralmanager%28_,willrestorestate%29.md) delegate method to reconstitute the restored state when the system launches your extension from a cold state. The system doesn’t call this method when your extension resumes from a warm suspended state, since the objects remain in memory.

## See Also

### Determining the communication method
- [var transport: AccessoryTransport?](./transport.md)
  A transport method that the session uses to communicate with the accessory.
- [var pushToken: Data?](./pushtoken.md)
  A token that identifies the iOS device to the Apple Push Notification service for routing accessory responses over the internet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/transportstaterestoreidentifier)*