# OBEXCreateVEvent

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Creates a formatted vEvent, ready to be sent over OBEX or whatever. You probably will embed the output in a vCalendar event.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
CFDataRefOBEXCreateVEvent(const char *inCharset, uint32_t inCharsetLength, const char *inEncoding, uint32_t inEncodingLength, const char *inEventStartDate, uint32_t inEventStartDateLength, const char *inEventEndDate, uint32_t inEventEndDateLength, const char *inAlarmDate, uint32_t inAlarmDateLength, const char *inCategory, uint32_t inCategoryLength, const char *inSummary, uint32_t inSummaryLength, const char *inLocation, uint32_t inLocationLength, const char *inXIRMCLUID, uint32_t inXIRMCLUIDLength);
```

#### Return Value

A valid CFDataRef - nil if we failed.

#### Discussion

All parameters are optional. The CFDataRef returned to you is NOT retained. Retain it if you want to keep it. Be aware that certain devices such as Ericsson phones MUST have certain fields, such as a start and end date.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X v10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inCharset`: The Charset the passed data is in. Pass in a #defined charset for ease of use.
- `inCharsetLength`: The length of the Charset passed data.
- `inEncoding`: The encoding of the summary and location fields.
- `inEventStartDate`: Start of event date, in the (ISO8601) format: YYYYMMDDTHHMMSS. e.g. 19960415T083000 = 8:30 am on April 15, 1996. All time values should be in LOCAL time.
- `inEventEndDate`: End of event date.
- `inAlarmDate`: Date of Alarm for event, in the format: YYYYMMDDTHHMMSS.
- `inCategory`: Category of event, such as “MEETING” or “PHONE CALL”.
- `inSummary`: Summary of event. Max length is 36 bytes. Longer will result in a bad argument error.
- `inLocation`: Summary of event. Max length is 20 bytes. Longer will result in a bad argument error.
- `inXIRMCLUID`: The IRMC Local Unique Identifier Label, max length 12 bytes. Longer will result in a bad argument error.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexcreatevevent)*