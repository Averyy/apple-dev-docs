# OBEXSessionGetAvailableCommandResponsePayloadLength

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Gets space available for your data for a particular command response you are trying to send.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
OBEXError OBEXSessionGetAvailableCommandResponsePayloadLength(OBEXSessionRef inSessionRef, OBEXOpCode inOpCode, OBEXMaxPacketLength *outLength);
```

#### Return Value

An error code value. 0 if successful.

#### Discussion

The OBEXSession takes care of packaging OBEX opcodes and other information into the proper packet format, allowing you to focus on sending the proper OBEX headers in your commands and command responses. This formatting and datas requires a small bit of information that varies depending on what command or response you are sending. Thus, you should call this function to find out how much space will be left for your headers before you send the command, allowing you to properly chop up your headers before sending them. This will guarantee that (a) you use up all the available space in a packet and (b) that you do not get an error trying to send too much information at once.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X v10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inSessionRef`: A valid session reference.
- `inOpCode`: A command opcode that you are responding to. For example, if you receiving a Put command, and want to send back a “bad request” response, you should still pass in the Put command opcode for that response.
- `outLength`: Space available for your header data in the payload area for a particular command.

## See Also

### Miscellaneous
- [GET_HEADER_ID_IS_NULL_TERMINATED_UNICODE_TEXT](./get_header_id_is_null_terminated_unicode_text.md)
  Convenience Macros for working with OBEX Header Identifiers.
- [func OBEXAddApplicationParameterHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddapplicationparameterheader%28_,_,_%29.md)
  Add bytes representing an application parameter to a dictionary of OBEX headers.
- [func OBEXAddAuthorizationChallengeHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddauthorizationchallengeheader%28_,_,_%29.md)
  Add an authorization challenge header to a dictionary of OBEXheaders.
- [func OBEXAddAuthorizationResponseHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddauthorizationresponseheader%28_,_,_%29.md)
  Add an authorization Response header to a dictionary of OBEXheaders.
- [func OBEXAddBodyHeader(UnsafeRawPointer!, UInt32, Bool, CFMutableDictionary!) -> OBEXError](./obexaddbodyheader%28_,_,_,_%29.md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddByteSequenceHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddbytesequenceheader%28_,_,_%29.md)
  Add a byte sequence header to a dictionary of OBEXheaders.
- [func OBEXAddConnectionIDHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddconnectionidheader%28_,_,_%29.md)
  Add bytes representing a connection ID to a dictionary of OBEX headers.
- [func OBEXAddCountHeader(UInt32, CFMutableDictionary!) -> OBEXError](./obexaddcountheader%28_,_%29.md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddDescriptionHeader(CFString!, CFMutableDictionary!) -> OBEXError](./obexadddescriptionheader%28_,_%29.md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddHTTPHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddhttpheader%28_,_,_%29.md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddLengthHeader(UInt32, CFMutableDictionary!) -> OBEXError](./obexaddlengthheader%28_,_%29.md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddNameHeader(CFString!, CFMutableDictionary!) -> OBEXError](./obexaddnameheader%28_,_%29.md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddObjectClassHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddobjectclassheader%28_,_,_%29.md)
  Add an object class header to a dictionary of OBEXheaders.
- [func OBEXAddTargetHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddtargetheader%28_,_,_%29.md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddTime4ByteHeader(UInt32, CFMutableDictionary!) -> OBEXError](./obexaddtime4byteheader%28_,_%29.md)
  Add a CFStringRef to a dictionary of OBEXheaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsessiongetavailablecommandresponsepayloadlength)*