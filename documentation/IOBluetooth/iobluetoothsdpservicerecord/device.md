# device

**Framework**: IOBluetooth  
**Kind**: property

Returns the IOBluetoothDevice that the target service belongs to.

**Availability**:
- macOS ?+

## Declaration

```swift
var device: IOBluetoothDevice! { get }
```

#### Return Value

Returns the IOBluetoothDevice that the target service belongs to. If the service is one the local host is vending, then nil is returned.

#### Discussion

If the service is a local service (i.e. one the current host is vending out), then nil is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/device)*