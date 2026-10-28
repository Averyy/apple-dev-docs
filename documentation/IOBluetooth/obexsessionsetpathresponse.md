# OBEXSessionSetPathResponse

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Send a response to a set path command to the remote client.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
OBEXError OBEXSessionSetPathResponse(OBEXSessionRef inSessionRef, OBEXOpCode inResponseOpCode, void *inOptionalHeaders, size_t inOptionalHeadersLength, OBEXSessionEventCallback inCallback, void *inUserRefCon);
```

## Return Value

An error code value. 0 if successful.

## Discussion

As all commands for OBEX sessions, this command is asynchronous only. A NULL callback paramter will result in an error.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X v10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inSessionRef`: A valid session reference.
- `inResponseOpCode`: What response code you want to send to the remote client.
- `inOptionalHeaders`: Ptr to optional headers you can supply to the command. DO NOT dispose of this pointer until you callback is called with a success.
- `inOptionalHeadersLength`: Size of data at the specified ptr.
- `inCallback`: A valid callback. Will be called for progress, errors and completion.
- `inUserRefCon`: Optional parameter; can contain anything you wish. Will be returned in your callback just as you passed it.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsessionsetpathresponse)*