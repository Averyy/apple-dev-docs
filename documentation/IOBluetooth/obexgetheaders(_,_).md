# OBEXGetHeaders(_:_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Take a data blob and looks for OBEX headers.

**Availability**:
- macOS

## Declaration

```swift
func OBEXGetHeaders(_ inData: UnsafeRawPointer!, _ inDataSize: Int) -> CFDictionary!
```

```c
CFDictionaryRefOBEXGetHeaders(const void *inData, size_t inDataSize);
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

### Miscellaneous
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
- [func OBEXAddTimeISOHeader(UnsafeRawPointer!, UInt32, CFMutableDictionary!) -> OBEXError](./obexaddtimeisoheader%28_,_,_%29.md)
  Add bytes to a dictionary of OBEXheaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexgetheaders(_:_:))*