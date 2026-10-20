# CFHTTPMessageAppendBytes(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Appends data to a `CFHTTPMessage` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageAppendBytes(_ message: CFHTTPMessage, _ newBytes: UnsafePointer<UInt8>, _ numBytes: CFIndex) -> Bool
```

```c
extern Boolean CFHTTPMessageAppendBytes(CFHTTPMessageRef message, const UInt8 *newBytes, CFIndex numBytes);
```

#### Return Value

`TRUE` if the data was successfully appended, otherwise `FALSE`.

#### Discussion

This function appends the data specified by `newBytes` to the specified message object which was created by calling [`CFHTTPMessageCreateEmpty(_:_:)`](./cfhttpmessagecreateempty%28_,_%29.md). The data is an incoming serialized HTTP request or response received from a client or a server. While appending the data, this function deserializes it, removes any HTTP-based formatting that the message may contain, and stores the message in the message object. You can then call [`CFHTTPMessageCopyVersion(_:)`](./cfhttpmessagecopyversion%28_%29.md), [`CFHTTPMessageCopyBody(_:)`](./cfhttpmessagecopybody%28_%29.md), [`CFHTTPMessageCopyHeaderFieldValue(_:_:)`](./cfhttpmessagecopyheaderfieldvalue%28_,_%29.md), and [`CFHTTPMessageCopyAllHeaderFields(_:)`](./cfhttpmessagecopyallheaderfields%28_%29.md) to get the message’s HTTP version, the message’s body, a specific header field, and all of the message’s headers, respectively.

If the message is a request, you can also call [`CFHTTPMessageCopyRequestURL(_:)`](./cfhttpmessagecopyrequesturl%28_%29.md) and [`CFHTTPMessageCopyRequestMethod(_:)`](./cfhttpmessagecopyrequestmethod%28_%29.md) to get the message’s request URL and request method, respectively.

If the message is a response, you can also call [`CFHTTPMessageGetResponseStatusCode(_:)`](./cfhttpmessagegetresponsestatuscode%28_%29.md) and [`CFHTTPMessageCopyResponseStatusLine(_:)`](./cfhttpmessagecopyresponsestatusline%28_%29.md) to get the message’s status code and status line, respectively.

## Parameters

- `message`: The message to modify.
- `newBytes`: A reference to the data to append.
- `numBytes`: The length of the data pointed to by `newBytes`.

## See Also

### HTTP Messages
- [class CFHTTPMessage](./cfhttpmessage.md)
  An opaque reference representing an HTTP message.
- [func CFHTTPMessageAddAuthentication(CFHTTPMessage, CFHTTPMessage?, CFString, CFString, CFString?, Bool) -> Bool](./cfhttpmessageaddauthentication%28_,_,_,_,_,_%29.md)
  Adds authentication information to a request.
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
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreaterequest%28_,_,_,_%29.md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageappendbytes(_:_:_:))*