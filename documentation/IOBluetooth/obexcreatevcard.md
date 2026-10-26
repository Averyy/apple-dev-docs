# OBEXCreateVCard

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Creates a formatted vCard, ready to be sent over OBEX or whatever.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
CFDataRefOBEXCreateVCard(const void *inFirstName, uint32_t inFirstNameLength, const void *inLastName, uint32_t inLastNameLength, const void *inFriendlyName, uint32_t inFriendlyNameLength, const void *inNameCharset, uint32_t inNameCharsetLength, const void *inHomePhone, uint32_t inHomePhoneLength, const void *inWorkPhone, uint32_t inWorkPhoneLength, const void *inCellPhone, uint32_t inCellPhoneLength, const void *inFaxPhone, uint32_t inFaxPhoneLength, const void *inEMailAddress, uint32_t inEMailAddressLength, const void *inEMailAddressCharset, uint32_t inEMailAddressCharsetLength, const void *inOrganization, uint32_t inOrganizationLength, const void *inOrganizationCharset, uint32_t inOrganizationCharsetLength, const void *inTitle, uint32_t inTitleLength, const void *inTitleCharset, uint32_t inTitleCharsetLength);
```

#### Return Value

An CFDataRef containing the compiled data. nil if we failed.

#### Discussion

All parameters are optional. The CFDataRef returned to you is NOT retained. Retain it if you want to keep it.

*** DEPRECATED IN BLUETOOTH 2.2 (OS X v10.6) *** You should transition your code to Objective-C equivalents. *** This API may be removed any time in the future.

## Parameters

- `inFirstName`: Pointer to data with Person’s first name.
- `inFirstNameLength`: Length of Person’s first name passed in above.
- `inLastName`: Pointer to data with Person’s last name.
- `inLastNameLength`: Length of Person’s last name passed in above.
- `inFriendlyName`: Pointer to data with Person’s Friendly name.
- `inFriendlyNameLength`: Length of Person’s Friendly name passed in above.
- `inNameCharset`: A pointer to the charset data used for the name. Pass in a #defined charset for ease of use.
- `inNameCharsetLength`: Length of name charset assed in above.
- `inHomePhone`: Pointer to data with Person’s Home phone number.
- `inHomePhoneLength`: Length of Person’s Home phone number passed in above.
- `inWorkPhone`: Work phone number.
- `inWorkPhoneLength`: Length of Person’s Work phone number passed in above.
- `inCellPhone`: Cell phone number.
- `inCellPhoneLength`: Length of Person’s Cell phone number passed in above.
- `inFaxPhone`: Fax phone number.
- `inFaxPhoneLength`: Length of Person’s Fax phone number passed in above.
- `inEMailAddress`: EMailAddress of person.
- `inEMailAddressLength`: Length of Person’s EMailAddress passed in above.
- `inEMailAddressCharset`: Charset of EMailAddress of person.
- `inEMailAddressCharsetLength`: Length of Person’s EMailAddress charset passed in above.
- `inOrganization`: Pointer to Organization/business data.
- `inOrganizationLength`: Length of Organization/business data.
- `inOrganizationCharset`: Pointer to the charset the Organization/business is in.

  Pointer to the charset the Title is in.
- `inOrganizationCharsetLength`: Length of data for the Organization/business charset.

  Length of data for the Title charset.
- `inTitle`: Pointer to data with Title of person in biz/org.
- `inTitleLength`: Length of Title of person in biz/org.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexcreatevcard)*