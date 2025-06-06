# CFHTTPMessageAddAuthentication(_:_:_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Adds authentication information to a request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageAddAuthentication(_ request: CFHTTPMessage, _ authenticationFailureResponse: CFHTTPMessage?, _ username: CFString, _ password: CFString, _ authenticationScheme: CFString?, _ forProxy: Bool) -> Bool
```

#### Return Value

`TRUE` if the authentication information was successfully added, otherwise `FALSE`.

#### Discussion

This function adds the authentication information specified by the `username`, `password`, `authenticationScheme`, and `forProxy` parameters to the specified request message. The message referred to by the `authenticationFailureResponse` parameter typically contains a 401 or a 407 error code.

This function is best suited for sending a single request to the server. If you need to send multiple requests, use [`CFHTTPMessageApplyCredentials(_:_:_:_:_:)`](cfhttpmessageapplycredentials(_:_:_:_:_:).md).

## Parameters

- `request`: The message to which to add authentication information.
- `authenticationFailureResponse`: The response message that contains authentication failure information.
- `username`: The username to add to the request.
- `password`: The password to add to the request.
- `authenticationScheme`: The authentication scheme to use ( ,  ,  , or  ), or pass   to use the strongest supported authentication scheme provided in the   parameter.
- `forProxy`: A flag indicating whether the authentication data that is being added is for a proxy’s use ( ) or for a remote server’s use ( ). If the error code provided by the   parameter is 407, set   to  . If the error code is 401, set   to  .

## See Also

- [class CFHTTPMessage](cfhttpmessage.md)
  An opaque reference representing an HTTP message.
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
- [func CFHTTPMessageCopySerializedMessage(CFHTTPMessage) -> Unmanaged<CFData>?](cfhttpmessagecopyserializedmessage(_:).md)
  Serializes a CFHTTPMessage object.
- [func CFHTTPMessageCopyVersion(CFHTTPMessage) -> Unmanaged<CFString>](cfhttpmessagecopyversion(_:).md)
  Gets the HTTP version from a `CFHTTPMessage` object.
- [func CFHTTPMessageCreateCopy(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreatecopy(_:_:).md)
  Gets a copy of a CFHTTPMessage object.
- [func CFHTTPMessageCreateEmpty(CFAllocator?, Bool) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreateempty(_:_:).md)
  Creates and returns a new, empty `CFHTTPMessage` object.
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](cfhttpmessagecreaterequest(_:_:_:_:).md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageaddauthentication(_:_:_:_:_:_:))*