# Current Call Information Constants

**Framework**: IOBluetooth

Get information about a phone call on a hands-free Bluetooth device.

## Topics

### Call Information
- [let IOBluetoothHandsFreeCallDirection: String](iobluetoothhandsfreecalldirection.md)
  A value that indicates whether a call is incoming or outgoing.
- [let IOBluetoothHandsFreeCallIndex: String](iobluetoothhandsfreecallindex.md)
  The index of the call, starting with `1`.
- [let IOBluetoothHandsFreeCallMode: String](iobluetoothhandsfreecallmode.md)
  The type of call data.
- [let IOBluetoothHandsFreeCallMultiparty: String](iobluetoothhandsfreecallmultiparty.md)
  A value that indicates whether the call is multiple-party.
- [let IOBluetoothHandsFreeCallStatus: String](iobluetoothhandsfreecallstatus.md)
  The current state of the call.
### Remote Number Information
- [let IOBluetoothHandsFreeCallNumber: String](iobluetoothhandsfreecallnumber.md)
  The caller’s phone number.
- [let IOBluetoothHandsFreeCallType: String](iobluetoothhandsfreecalltype.md)
  The format of the caller’s phone number.
- [let IOBluetoothHandsFreeCallName: String](iobluetoothhandsfreecallname.md)
  The name of the caller.

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:incomingcallfrom:).md)
  Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.
- [func handsFree(IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)](iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:).md)
  Sends the delegate information about the current call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/current-call-information-constants)*