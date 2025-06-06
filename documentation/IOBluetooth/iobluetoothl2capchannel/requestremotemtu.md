# requestRemoteMTU(_:)

**Framework**: IOBluetooth  
**Kind**: method

Initiates the process to reconfigure the L2CAP channel with a new outgoing MTU.

**Availability**:
- macOS ?+

## Declaration

```swift
func requestRemoteMTU(_ remoteMTU: BluetoothL2CAPMTU) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the channel re-configure process was successfully initiated.

#### Discussion

Currently, this API does not give an indication that the re-config process has completed. In the future additional API will be available to provide that information both synchronously and asynchronously.

## Parameters

- `remoteMTU`: The desired outgoing MTU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/requestremotemtu(_:))*