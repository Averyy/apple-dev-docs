# OBEXSessionGetAvailableCommandPayloadLength

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Gets space available for your data for a particular command response you are trying to send.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
OBEXError OBEXSessionGetAvailableCommandPayloadLength(OBEXSessionRef inSessionRef, OBEXOpCode inOpCode, OBEXMaxPacketLength *outLength);
```

#### Return Value

An error code value. 0 if successful.

#### Overview

The OBEXSession takes care of packaging OBEX opcodes and other information into the proper packet format, allowing you to focus on sending the proper OBEX headers in your commands and command responses. This formatting and datas requires a small bit of information that varies depending on what command or response you are sending. Thus, you should call this function to find out how much space will be left for your headers before you send the command, allowing you to properly chop up your headers before sending them. This will guarantee that (a) you use up all the available space in a packet and (b) that you do not get an error trying to send too much information at once.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X v10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inSessionRef`: A valid session reference.
- `inOpCode`: A command opcode that you are responding to. For example, if you receiving a Put command, and want to send back a “bad request” response, you should still pass in the Put command opcode for that response.
- `outLength`: Space available for your header data in the payload area for a particular command.

## See Also

### Functions
- [func IOBluetoothNSStringFromDeviceAddressColon(UnsafePointer<BluetoothDeviceAddress>!) -> String!](./iobluetoothnsstringfromdeviceaddresscolon%28_%29.md)
- [func IOBluetoothPackDataList(UnsafeMutableRawPointer!, UnsafePointer<CChar>!, CVaListPointer) -> Int](./iobluetoothpackdatalist%28_,_,_%29.md)
- [func IOBluetoothUnpackDataList(Int, UnsafeRawPointer!, UnsafePointer<CChar>!, CVaListPointer) -> Int](./iobluetoothunpackdatalist%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsessiongetavailablecommandpayloadlength)*