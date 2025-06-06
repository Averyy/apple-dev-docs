# CFReadStreamCreateForStreamedHTTPRequest(_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFReadStreamCreateForStreamedHTTPRequest(_ alloc: CFAllocator?, _ requestHeaders: CFHTTPMessage, _ requestBody: CFReadStream) -> Unmanaged<CFReadStream>
```

#### Return Value

A new read stream, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates a read stream for the response to the `requestHeaders` plus `requestBody`. Call this function instead of [`CFReadStreamCreateForHTTPRequest(_:_:)`](cfreadstreamcreateforhttprequest(_:_:).md) when the body of the request is so long that you do not want it to be resident in memory.

Because streams cannot be reset, read streams created this way cannot be enabled for autoredirection.

If the Content-Length header is set in `requestHeaders`, it is assumed that the length is correct and that `requestBody` will report end-of-stream after precisely Content-Length bytes have been read from it. If the Content-Length header is not set, the chunked transfer-encoding will be added to `requestHeaders`, and bytes read from `requestBody` will be transmitted chunked. The body of `requestHeaders` is ignored.

After creating the read stream, you can call [`CFReadStreamGetError(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamGetError(_:)) at any time to check the status of the stream. You may want to call `CFHTTPReadStreamSetProxy` to set the name and port number for a proxy. To serialize the request and send it, call [`CFReadStreamOpen(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamOpen(_:)).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `requestHeaders`: A CFHTTP request header.
- `requestBody`: Read stream reference for the request body.

## See Also

- [func CFReadStreamCreateForHTTPRequest(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFReadStream>](cfreadstreamcreateforhttprequest(_:_:).md)
  Creates a read stream for a CFHTTP request message.
- [let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString](kcfstreampropertyhttpattemptpersistentconnection.md)
- [let kCFStreamPropertyHTTPFinalRequest: CFString](kcfstreampropertyhttpfinalrequest.md)
  HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set.
- [let kCFStreamPropertyHTTPFinalURL: CFString](kcfstreampropertyhttpfinalurl.md)
  HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set.
- [let kCFStreamPropertyHTTPProxy: CFString](kcfstreampropertyhttpproxy.md)
- [let kCFStreamPropertyHTTPProxyHost: CFString](kcfstreampropertyhttpproxyhost.md)
- [let kCFStreamPropertyHTTPProxyPort: CFString](kcfstreampropertyhttpproxyport.md)
- [let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString](kcfstreampropertyhttprequestbyteswrittencount.md)
- [let kCFStreamPropertyHTTPResponseHeader: CFString](kcfstreampropertyhttpresponseheader.md)
  HTTP Response Header property. When copied by [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)), the header of an HTTP response message is returned.
- [let kCFStreamPropertyHTTPSProxyHost: CFString](kcfstreampropertyhttpsproxyhost.md)
- [let kCFStreamPropertyHTTPSProxyPort: CFString](kcfstreampropertyhttpsproxyport.md)
- [let kCFStreamPropertyHTTPShouldAutoredirect: CFString](kcfstreampropertyhttpshouldautoredirect.md)
  HTTP Should Auto Redirect property. Set this property to `kCFBooleanTrue` to enable autoredirection; set this property to `kCFBooleanFalse` to disable autoredirection.
- [func CFWriteStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFWriteStream>](cfwritestreamcreatewithftpurl(_:_:).md)
  Creates an FTP write stream.
- [func CFReadStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFReadStream>](cfreadstreamcreatewithftpurl(_:_:).md)
  Creates an FTP read stream.
- [let kCFStreamPropertyFTPAttemptPersistentConnection: CFString](kcfstreampropertyftpattemptpersistentconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfreadstreamcreateforstreamedhttprequest(_:_:_:))*