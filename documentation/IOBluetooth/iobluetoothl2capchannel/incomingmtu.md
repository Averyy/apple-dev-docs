# incomingMTU

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Returns the current incoming MTU for the L2CAP channel.

**Availability**:
- macOS

## Declaration

```swift
var incomingMTU: BluetoothL2CAPMTU { get }
```

```objc
@property (readonly) BluetoothL2CAPMTU incomingMTU;
```

## Discussion

The incoming MTU represents the maximum L2CAP packet size for packets being sent by the remote device.

## See Also

### Related Documentation
- [- getIncomingMTU](./getincomingmtu.md)
  Returns the current incoming MTU for the L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/incomingmtu)*