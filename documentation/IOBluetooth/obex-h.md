# OBEX.h

**Framework**: IOBluetooth

Public OBEX technology interfaces.

#### Overview

Contains generic OBEX constants, structs, and C API used for all OBEX communication over any transport. For specific transport API, see that transport’s C API. For example, if you wanted to know more about the Bluetooth OBEX implementation, see OBEXBluetooth.h.

The file also contains API that will assist in the construction and deconstruction of OBEX headers to and from raw bytes, as well as the creation of vCards and vEvents.

##### Included Headers

- <stdio.h>
- <stdint.h>
- <CoreServices/CoreServices.h>
- <IOBluetooth/IOBluetoothUserLib.h>

## Topics

### Miscellaneous
- [func OBEXAddApplicationParameterHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddapplicationparameterheader(_:_:_:).md)
  Add bytes representing an application parameter to a dictionary of OBEX headers.
- [func OBEXAddAuthorizationChallengeHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddauthorizationchallengeheader(_:_:_:).md)
  Add an authorization challenge header to a dictionary of OBEXheaders.
- [func OBEXAddAuthorizationResponseHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddauthorizationresponseheader(_:_:_:).md)
  Add an authorization Response header to a dictionary of OBEXheaders.
- [func OBEXAddBodyHeader(UnsafeRawPointer!, UInt32, Bool, CFMutableDictionary!) -> OBEXError](obexaddbodyheader(_:_:_:_:).md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXAddByteSequenceHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddbytesequenceheader(_:_:_:).md)
  Add a byte sequence header to a dictionary of OBEXheaders.
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
- [func OBEXAddUserDefinedHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexadduserdefinedheader(_:_:_:).md)
  Add a user-defined custom header to a dictionary of OBEXheaders.
- [func OBEXAddWhoHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](obexaddwhoheader(_:_:_:).md)
  Add bytes of data to a dictionary of OBEXheaders.
- [func OBEXGetHeaders(UnsafeRawPointer!, Int) -> CFDictionary!](obexgetheaders(_:_:).md)
  Take a data blob and looks for OBEX headers.
- [func OBEXHeadersToBytes(CFDictionary!) -> Unmanaged<CFMutableData>!](obexheaderstobytes(_:).md)
  Converts a dictionary of headers to a data pointer, from which you can extract as bytes and pass to the OBEX command/response functions.
### Data Types
- [struct OBEXSessionEvent](obexsessionevent.md)
- [struct OBEXAbortCommandData](obexabortcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXAbortCommandResponseData](obexabortcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandData](obexconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXConnectCommandResponseData](obexconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandData](obexdisconnectcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXDisconnectCommandResponseData](obexdisconnectcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXErrorData](obexerrordata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandData](obexgetcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXGetCommandResponseData](obexgetcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandData](obexputcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXPutCommandResponseData](obexputcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandData](obexsetpathcommanddata.md)
  Part of the OBEXSessionEvent structure.
- [struct OBEXSetPathCommandResponseData](obexsetpathcommandresponsedata.md)
  Part of the OBEXSessionEvent structure.
### Constants
- [struct OBEXConnectFlagValues](obexconnectflagvalues.md)
  Flags for Connect command.
- [typealias OBEXError](obexerror.md)
  Codes for OBEX errors. If the return value was not in the following range, then it is most likely resulting from kernel code/IOKit, and you should consult IOReturn.h for those codes.
- [struct OBEXHeaderIdentifiers](obexheaderidentifiers.md)
  Identifiers for OBEX Headers.
- [struct OBEXNonceFlagValues](obexnonceflagvalues.md)
  Flags for Nonce command during digest challenge.
- [struct OBEXOpCodeCommandValues](obexopcodecommandvalues.md)
  Operation OpCode values for commands.
- [struct OBEXOpCodeResponseValues](obexopcoderesponsevalues.md)
  Response opCode values.
- [struct OBEXOpCodeSessionValues](obexopcodesessionvalues.md)
  Operation OpCode values for sessions. From the OBEX 1.3 specification.
- [struct OBEXPutFlagValues](obexputflagvalues.md)
- [struct OBEXRealmValues](obexrealmvalues.md)
  Values for Realm during digest response.
- [struct OBEXSessionEventTypes](obexsessioneventtypes.md)
  Type identifiers for OBEX sessions.
- [struct OBEXSessionParameterTags](obexsessionparametertags.md)
  Tags for SessionParameters.
- [struct OBEXVersions](obexversions.md)
  The available/supported OBEX versions.
### Macros
- [OBEX Convenience Macros](obex-convenience-macros.md)
  Convenience Macros for working with OBEX Header Identifiers.

## See Also

- [Bluetooth.h User-Space](bluetooth-h-user-space.md)
  Bluetooth wireless technology
- [IOBluetoothUserLib.h](iobluetoothuserlib-h.md)
  Public Interfaces for Apple’s implementation of Bluetooth technology.
- [IOBluetoothUtilities.h](iobluetoothutilities-h.md)
  See the Overview section above for header-level documentation.
- [OBEXBluetooth.h](obexbluetooth-h.md)
  Object Exchange over Bluetooth.
- [OBEXFileTransferServices.h](obexfiletransferservices-h.md)
- [IOBluetooth Structures](iobluetooth-structures.md)
- [IOBluetooth Enumerations](iobluetooth-enumerations.md)
- [IOBluetooth Constants](iobluetooth-constants.md)
- [IOBluetooth Functions](iobluetooth-functions.md)
- [IOBluetooth Data Types](iobluetooth-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obex-h)*