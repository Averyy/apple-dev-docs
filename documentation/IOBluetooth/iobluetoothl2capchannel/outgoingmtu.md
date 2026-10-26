# outgoingMTU

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Returns the current outgoing MTU for the L2CAP channel.

**Availability**:
- macOS

## Declaration

```swift
var outgoingMTU: BluetoothL2CAPMTU { get }
```

```objc
@property (readonly) BluetoothL2CAPMTU outgoingMTU;
```

#### Discussion

The outgoing MTU represents the maximum L2CAP packet size for packets being sent to the remote device.

## See Also

### Related Documentation
- [- getOutgoingMTU](./getoutgoingmtu.md)
  Returns the current outgoing MTU for the L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/outgoingmtu)*