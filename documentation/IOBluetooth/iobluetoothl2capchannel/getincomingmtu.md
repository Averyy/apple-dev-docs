# getIncomingMTU

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Returns the current incoming MTU for the L2CAP channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (BluetoothL2CAPMTU) getIncomingMTU;
```

## Return Value

Returns the current incoming MTU for the L2CAP channel.

## Discussion

The incoming MTU represents the maximum L2CAP packet size for packets being sent by the remote device.

## See Also

### Related Documentation
- [var incomingMTU: BluetoothL2CAPMTU](./incomingmtu.md)
  Returns the current incoming MTU for the L2CAP channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/getincomingmtu)*