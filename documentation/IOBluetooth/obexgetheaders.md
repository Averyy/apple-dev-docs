# OBEXGetHeaders(_:_:)

**Framework**: IOBluetooth  
**Kind**: func

Take a data blob and looks for OBEX headers.

**Availability**:
- macOS ?+

## Declaration

```swift
func OBEXGetHeaders(_ inData: UnsafeRawPointer!, _ inDataSize: Int) -> CFDictionary!
```

#### Return Value

A CFDictionary with the headers found in the data blob inside it.

#### Discussion

You should use this when your callback for PUTs, GETs, etc. give you a data chunk and a size. Pass these params to this function and you will receive a dictionary back full of the parse headers. You can use the CFDictionary calls to get objects out of it, based on the header keys defined above. You are responsible for releasing the CFDictionary returned to you. Example usage:

```objc
 
   CFDictionaryRef   dictionary = OBEXGetHeaders( data, dataLength );
   if( dictionary )
   {
   	if( CFDictionaryGetCountOfKey( dictionary, kOBEXHeaderIDKeyName ) > 0 )
   	{
   		CFStringRef theStringRef;
 
   		theStringRef = (CFStringRef) CFDictionaryGetValue( dictionary, kOBEXHeaderIDKeyName );
   		if( theStringRef )
   		{
   			// Display it, use it as a filename, whatever.
   		}
   	}
 
   	if( CFDictionaryGetCountOfKey( dictionary, kOBEXHeaderIDKeyConnectionID ) > 0 )
   	{
   		CFDataRef theDataRef;
 
   		theDataRef = (CFDataRef) CFDictionaryGetValue( dictionary, kOBEXHeaderIDKeyConnectionID );
   		if( theDataRef )
   		{
   			// now we have data representing the connection ID.
   		}
   	}
 
   	CFRelease( dictionary );
   }
 
```

## Parameters

- `inData`: The data chunk with the headers you are interested in.
- `inDataSize`: The size of the buffer you are passing in.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexgetheaders(_:_:))*