# CFHTTPMessageAddAuthentication(_:_:_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CFHTTPMessageAddAuthentication(CFHTTPMessageRef request, CFHTTPMessageRef authenticationFailureResponse, CFStringRef username, CFStringRef password, CFStringRef authenticationScheme, Boolean forProxy);
```

#### Return Value

`TRUE` if the authentication information was successfully added, otherwise `FALSE`.

#### Discussion

This function adds the authentication information specified by the `username`, `password`, `authenticationScheme`, and `forProxy` parameters to the specified request message. The message referred to by the `authenticationFailureResponse` parameter typically contains a 401 or a 407 error code.

This function is best suited for sending a single request to the server. If you need to send multiple requests, use [`CFHTTPMessageApplyCredentials(_:_:_:_:_:)`](./cfhttpmessageapplycredentials%28_,_,_,_,_%29.md).

## Parameters

- `request`: The message to which to add authentication information.
- `authenticationFailureResponse`: The response message that contains authentication failure information.
- `username`: The username to add to the request.
- `password`: The password to add to the request.
- `authenticationScheme`: The authentication scheme to use (`kCFHTTPAuthenticationSchemeBasic`, `kCFHTTPAuthenticationSchemeNegotiate`, `kCFHTTPAuthenticationSchemeNTLM`, or `kCFHTTPAuthenticationSchemeDigest`), or pass `NULL` to use the strongest supported authentication scheme provided in the `authenticationFailureResponse` parameter.
- `forProxy`: A flag indicating whether the authentication data that is being added is for a proxy’s use (`TRUE`) or for a remote server’s use (`FALSE`). If the error code provided by the `authenticationFailureResponse` parameter is 407, set `forProxy` to `TRUE`. If the error code is 401, set `forProxy` to `FALSE`.

## See Also

### HTTP Messages
- [class CFHTTPMessage](./cfhttpmessage.md)
  An opaque reference representing an HTTP message.
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
- [func CFHTTPMessageCreateRequest(CFAllocator?, CFString, CFURL, CFString) -> Unmanaged<CFHTTPMessage>](./cfhttpmessagecreaterequest%28_,_,_,_%29.md)
  Creates and returns a `CFHTTPMessage` object for an HTTP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageaddauthentication(_:_:_:_:_:_:))*