# getOutgoingMTU

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Returns the current outgoing MTU for the L2CAP channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothL2CAPMTU) getOutgoingMTU;
```

#### Return Value

Returns the current outgoing MTU for the L2CAP channel.

#### Discussion

The outgoing MTU represents the maximum L2CAP packet size for packets being sent to the remote device.

## See Also

### Related Documentation
- [var outgoingMTU: BluetoothL2CAPMTU](./outgoingmtu.md)
  Returns the current outgoing MTU for the L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/getoutgoingmtu)*