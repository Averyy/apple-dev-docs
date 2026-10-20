# CFHTTPMessageCreateResponse(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Creates and returns a `CFHTTPMessage` object for an HTTP response.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageCreateResponse(_ alloc: CFAllocator?, _ statusCode: CFIndex, _ statusDescription: CFString?, _ httpVersion: CFString) -> Unmanaged<CFHTTPMessage>
```

```c
extern CFHTTPMessageRefCFHTTPMessageCreateResponse(CFAllocatorRef alloc, CFIndex statusCode, CFStringRef statusDescription, CFStringRef httpVersion);
```

#### Return Value

A new `CFHTTPMessage` object, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function returns a `CFHTTPMessage` object that you can use to build an HTTP response. Continue building the response by calling[`CFHTTPMessageSetBody(_:_:)`](./cfhttpmessagesetbody%28_,_%29.md) to set the message’s body. Call [`CFHTTPMessageSetHeaderFieldValue(_:_:_:)`](./cfhttpmessagesetheaderfieldvalue%28_,_,_%29.md) to set the message’s headers. Then call [`CFHTTPMessageCopySerializedMessage(_:)`](./cfhttpmessagecopyserializedmessage%28_%29.md) to make the message ready for transmission by serializing it.

## Parameters

- `statusCode`: The status code for this message response. The status code can be any of the status codes defined in section 6.1.1 of RFC 2616.
- `statusDescription`: The description that corresponds to the status code. Pass NULL to use the standard description for the given status code, as found in RFC 2616.
- `httpVersion`: The HTTP version for this message response. Pass `kCFHTTPVersion1_0` or `kCFHTTPVersion1_1`.

## See Also

### HTTP Messages
- [class CFHTTPMessage](./cfhttpmessage.md)
  An opaque reference representing an HTTP message.
- [func CFHTTPMessageAddAuthentication(CFHTTPMessage, CFHTTPMessage?, CFString, CFString, CFString?, Bool) -> Bool](./cfhttpmessageaddauthentication%28_,_,_,_,_,_%29.md)
  Adds authentication information to a request.
- [func CFHTTPMessageAppendBytes(CFHTTPMessage, UnsafePointer<UInt8>, CFIndex) -> Bool](./cfhttpmessageappendbytes%28_,_,_%29.md)
  Appends data to a `CFHTTPMessage` object.
- [func CFHTTPMessageApplyCredentialDictionary(CFHTTPMessage, CFHTTPAuthentication, CFDictionary, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfhttpmessageapplycredentialdictionary%28_,_,_,_%29.md)
  Use a dictionary containing authentication credentials to perform the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageApplyCredentials(CFHTTPMessage, CFHTTPAuthentication, CFString?, CFString?, UnsafeMutablePointer<CFStreamError>?) -> Bool](./cfhttpmessageapplycredentials%28_,_,_,_,_%29.md)
  Performs the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageCopyAllHeaderFields(CFHTTPMessage) -> Unmanaged<CFDictionary>?](./cfhttpmessagecopyallheaderfields%28_%29.md)
  Gets all header fields from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyBody(CFHTTPMessage) -> Unmanaged<CFData>?](./cfhttpmessagecopybody%28_%29.md)
  Gets the body from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyHeaderFieldValue(CFHTTPMessage, CFString) -> Unmanaged<CFString>?](./cfhttpmessagecopyheaderfieldvalue%28_,_%29.md)
  Gets the value of a header field from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestMethod(CFHTTPMessage) -> Unmanaged<CFString>?](./cfhttpmessagecopyrequestmethod%28_%29.md)
  Gets the request method from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestURL(CFHTTPMessage) -> Unmanaged<CFURL>?](./cfhttpmessagecopyrequesturl%28_%29.md)
  Gets the URL from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyResponseStatusLine(CFHTTPMessage) -> Unmanaged<CFString>?](./cfhttpmessagecopyresponsestatusline%28_%29.md)
  Gets the status line from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopySerializedMessage(CFHTTPMessage) -> Unmanaged<CFData>?](./cfhttpmessagecopyserializedmessage%28_%29.md)
  Serializes a CFHTTPMessage object.
- [func CFHTTPMessageCopyVersion(CFHTTPMessage) -> Unmanaged<CFString>](./cfhttpmessagecopyversion%28_%29.md)
  Gets the HTTP version from a `CFHTTPMessage` object.
- [func CFHTTPMessageCreateCopy(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreatecopy%28_,_%29.md)
  Gets a copy of a CFHTTPMessage object.
- [func CFHTTPMessageCreateEmpty(CFAllocator?, Bool) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreateempty%28_,_%29.md)
  Creates and returns a new, empty `CFHTTPMessage` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecreateresponse(_:_:_:_:))*