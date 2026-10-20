# SMS Dictionary Key Constants

**Framework**: IOBluetooth  
**Role**: API Collection

Read the parts of an SMS message.

## Topics

### Sender Information
- [let IOBluetoothPDUOriginatingAddress: String](./iobluetoothpduoriginatingaddress.md)
  The phone number for the sender of the text message.
- [let IOBluetoothPDUOriginatingAddressType: String](./iobluetoothpduoriginatingaddresstype.md)
  The format of the phone number for the sender of the text message.
- [let IOBluetoothPDUServicCenterAddress: String](./iobluetoothpduserviccenteraddress.md)
  The phone number for the service center that stored and then delivered the message.
- [let IOBluetoothPDUServiceCenterAddressType: String](./iobluetoothpduservicecenteraddresstype.md)
  The format of the phone number for the service center.
### Message Information
- [let IOBluetoothPDUProtocolID: String](./iobluetoothpduprotocolid.md)
  The protocol of the text message content.
- [let IOBluetoothPDUUserData: String](./iobluetoothpduuserdata.md)
  The content of the text message.
- [let IOBluetoothPDUTimestamp: String](./iobluetoothpdutimestamp.md)
  The time the text message was sent.
- [let IOBluetoothPDUType: String](./iobluetoothpdutype.md)
  The GSM type of the text message.
- [let IOBluetoothPDUEncoding: String](./iobluetoothpduencoding.md)
  The encoding for the text message.

## See Also

### Receiving SMS Information
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingSMS: [AnyHashable : Any]!)](./iobluetoothhandsfreedevicedelegate/handsfree%28_,incomingsms%29.md)
  Tells the delegate there’s an incoming text message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/sms-dictionary-key-constants)*