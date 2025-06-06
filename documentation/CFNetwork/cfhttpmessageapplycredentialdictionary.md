# CFHTTPMessageApplyCredentialDictionary(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Use a dictionary containing authentication credentials to perform the authentication method specified by a `CFHTTPAuthentication` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage, _ auth: CFHTTPAuthentication, _ dict: CFDictionary, _ error: UnsafeMutablePointer<CFStreamError>?) -> Bool
```

#### Return Value

`TRUE` if the authentication was successful, otherwise, `FALSE`.

#### Discussion

This function performs the authentication method specified by `auth` on behalf of the request specified by `request` using the credentials contained in the dictionary specified by `dict`. The dictionary must contain values for the `kCFHTTPAuthenticationUsername` and `kCFHTTPAuthenticationPassword` keys. If [`CFHTTPAuthenticationRequiresAccountDomain(_:)`](cfhttpauthenticationrequiresaccountdomain(_:).md) returns `TRUE` for `auth`, the dictionary must also contain a value for the `kCFHTTPAuthenticationAccountDomain` key.

##### Special Considerations

This function is thread safe as long as another thread does not alter the same `CFHTTPAuthentication` object at the same time.

## Parameters

- `request`: The request for which the authentication method is to be performed.
- `auth`: A   object specifying the authentication method to perform.
- `dict`: A dictionary containing authentication credentials to be applied to the request. For information on the keys in this dictionary, see  .
- `error`: If an error occurs, upon return contains a   object that describes the error and the error’s domain. Pass   if you don’t want to receive error information.

## See Also

- [class CFHTTPMessage](cfhttpmessage.md)
  An opaque reference representing an HTTP message.
- [func CFHTTPMessageAddAuthentication(CFHTTPMessage, CFHTTPMessage?, CFString, CFString, CFString?, Bool) -> Bool](cfhttpmessageaddauthentication(_:_:_:_:_:_:).md)
  Adds authentication information to a request.
- [func CFHTTPMessageAppendBytes(CFHTTPMessage, UnsafePointer<UInt8>, CFIndex) -> Bool](cfhttpmessageappendbytes(_:_:_:).md)
  Appends data to a `CFHTTPMessage` object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageapplycredentialdictionary(_:_:_:_:))*