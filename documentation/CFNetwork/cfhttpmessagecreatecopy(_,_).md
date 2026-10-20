# CFHTTPMessageCreateCopy(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Gets a copy of a CFHTTPMessage object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageCreateCopy(_ alloc: CFAllocator?, _ message: CFHTTPMessage) -> Unmanaged<CFHTTPMessage>
```

```c
extern CFHTTPMessageRefCFHTTPMessageCreateCopy(CFAllocatorRef alloc, CFHTTPMessageRef message);
```

#### Return Value

A [`CFHTTPMessage`](./cfhttpmessage.md) object, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function returns a copy of a [`CFHTTPMessage`](./cfhttpmessage.md) object that you can modify, for example, by calling [`CFHTTPMessageCopyHeaderFieldValue(_:_:)`](./cfhttpmessagecopyheaderfieldvalue%28_,_%29.md) or by calling [`CFHTTPMessageSetBody(_:_:)`](./cfhttpmessagesetbody%28_,_%29.md). Then you can serialize the message by calling [`CFHTTPMessageCopySerializedMessage(_:)`](./cfhttpmessagecopyserializedmessage%28_%29.md) and send the serialized message to a client or a server.

## Parameters

- `message`: The message to copy.

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
- [func CFHTTPMessageCreateEmpty(CFAllocator?, Bool) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreateempty%28_,_%29.md)
  Creates and returns a new, empty `CFHTTPMessage` object.
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreaterequest%28_,_,_,_%29.md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecreatecopy(_:_:))*