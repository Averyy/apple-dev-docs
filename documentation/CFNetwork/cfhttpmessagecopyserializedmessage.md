# CFHTTPMessageCopySerializedMessage(_:)

**Framework**: CFNetwork  
**Kind**: func

Serializes a CFHTTPMessage object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageCopySerializedMessage(_ message: CFHTTPMessage) -> Unmanaged<CFData>?
```

#### Return Value

A `CFData` object containing the serialized message, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function returns a copy of a `CFHTTPMessage` object in serialized format that is ready for transmission.

## See Also

- [class CFHTTPMessage](cfhttpmessage.md)
  An opaque reference representing an HTTP message.
- [func CFHTTPMessageAddAuthentication(CFHTTPMessage, CFHTTPMessage?, CFString, CFString, CFString?, Bool) -> Bool](cfhttpmessageaddauthentication(_:_:_:_:_:_:).md)
  Adds authentication information to a request.
- [func CFHTTPMessageAppendBytes(CFHTTPMessage, UnsafePointer<UInt8>, CFIndex) -> Bool](cfhttpmessageappendbytes(_:_:_:).md)
  Appends data to a `CFHTTPMessage` object.
- [func CFHTTPMessageApplyCredentialDictionary(CFHTTPMessage, CFHTTPAuthentication, CFDictionary, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpmessageapplycredentialdictionary(_:_:_:_:).md)
  Use a dictionary containing authentication credentials to perform the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageApplyCredentials(CFHTTPMessage, CFHTTPAuthentication, CFString?, CFString?, UnsafeMutablePointer<CFStreamError>?) -> Bool](cfhttpmessageapplycredentials(_:_:_:_:_:).md)
  Performs the authentication method specified by a `CFHTTPAuthentication` object.
- [func CFHTTPMessageCopyAllHeaderFields(CFHTTPMessage) -> Unmanaged<CFDictionary>?](cfhttpmessagecopyallheaderfields(_:).md)
  Gets all header fields from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyBody(CFHTTPMessage) -> Unmanaged<CFData>?](cfhttpmessagecopybody(_:).md)
  Gets the body from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyHeaderFieldValue(CFHTTPMessage, CFString) -> Unmanaged<CFString>?](cfhttpmessagecopyheaderfieldvalue(_:_:).md)
  Gets the value of a header field from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestMethod(CFHTTPMessage) -> Unmanaged<CFString>?](cfhttpmessagecopyrequestmethod(_:).md)
  Gets the request method from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyRequestURL(CFHTTPMessage) -> Unmanaged<CFURL>?](cfhttpmessagecopyrequesturl(_:).md)
  Gets the URL from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyResponseStatusLine(CFHTTPMessage) -> Unmanaged<CFString>?](cfhttpmessagecopyresponsestatusline(_:).md)
  Gets the status line from a `CFHTTPMessage` object.
- [func CFHTTPMessageCopyVersion(CFHTTPMessage) -> Unmanaged<CFString>](cfhttpmessagecopyversion(_:).md)
  Gets the HTTP version from a `CFHTTPMessage` object.
- [func CFHTTPMessageCreateCopy(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreatecopy(_:_:).md)
  Gets a copy of a CFHTTPMessage object.
- [func CFHTTPMessageCreateEmpty(CFAllocator?, Bool) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreateempty(_:_:).md)
  Creates and returns a new, empty `CFHTTPMessage` object.
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreaterequest(_:_:_:_:).md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyserializedmessage(_:))*