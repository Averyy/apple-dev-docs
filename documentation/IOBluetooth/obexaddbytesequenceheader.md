# OBEXAddByteSequenceHeader(_:_:_:)

**Framework**: IOBluetooth  
**Kind**: func

Add a byte sequence header to a dictionary of OBEXheaders.

**Availability**:
- macOS ?+

## Declaration

```swift
func OBEXAddByteSequenceHeader(_ inHeaderData: UnsafeRawPointer!, _ inHeaderDataLength: UInt32, _ dictRef: CFMutableDictionary!) -> OBEXError
```

#### Return Value

Error code, kOBEXSuccess (0) if success.

#### Discussion

Byte Sequence header - OBEX Spec, 2.2.5: Byte sequence. One thing of important note here - since we don’t know what Header Identifier and length you intend to use here, you MUST include your own identifier and length in the data you pass. Thus, your data must be in this format: <1:HI><2:LENGTH><n:()> Also, note that LENGTH = (3 + n), (1 for HI, 2 for the 2 bytes of length information, plus your n bytes of custom data). Be careful here to not mess up these values, as it could adversely affect the ability of the remote-device’s headers parser.

## Parameters

- `inHeaderData`: Bytes you want to put in the byte sequence header.
- `inHeaderDataLength`: Length of the bytes you want to put in the byte sequence header.
- `dictRef`: Dictionary you have allocated to hold the headers. Make sure it’s mutable.

## See Also

- [func OBEXAddApplicationParameterHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddapplicationparameterheader(_:_:_:).md)
  Add bytes representing an application parameter to a dictionary of OBEX headers.
- [func OBEXAddAuthorizationChallengeHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddauthorizationchallengeheader(_:_:_:).md)
  Add an authorization challenge header to a dictionary of OBEXheaders.
- [func OBEXAddAuthorizationResponseHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddauthorizationresponseheader(_:_:_:).md)
  Add an authorization Response header to a dictionary of OBEXheaders.
- [func OBEXAddBodyHeader(UnsafeRawPointer!, UInt32, Bool, CFMutableDictionary!) -> OBEXError](obexaddbodyheader(_:_:_:_:).md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddConnectionIDHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddconnectionidheader(_:_:_:).md)
  Add bytes representing a connection ID to a dictionary of OBEX headers.
- [func OBEXAddCountHeader(UInt32, CFMutableDictionary!) -> OBEXError](obexaddcountheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddDescriptionHeader(CFString!, CFMutableDictionary!) -> OBEXError](obexadddescriptionheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddHTTPHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddhttpheader(_:_:_:).md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddLengthHeader(UInt32, CFMutableDictionary!) -> OBEXError](obexaddlengthheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddNameHeader(CFString!, CFMutableDictionary!) -> OBEXError](obexaddnameheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddObjectClassHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddobjectclassheader(_:_:_:).md)
  Add an object class header to a dictionary of OBEXheaders.
- [func OBEXAddTargetHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddtargetheader(_:_:_:).md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddTime4ByteHeader(UInt32, CFMutableDictionary!) -> OBEXError](obexaddtime4byteheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.
- [func OBEXAddTimeISOHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddtimeisoheader(_:_:_:).md)
  Add bytes to a dictionary of OBEXheaders.
- [func OBEXAddTypeHeader(CFString!, CFMutableDictionary!) -> OBEXError](obexaddtypeheader(_:_:).md)
  Add a CFStringRef to a dictionary of OBEXheaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexaddbytesequenceheader(_:_:_:))*