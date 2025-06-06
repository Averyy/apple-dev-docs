# kCFStreamPropertyFTPProxy

**Framework**: CFNetwork  
**Kind**: var

FTP Proxy stream property key for set and copy operations. The property is a value of type CFDictionary that holds proxy dictionary key-value pairs. The dictionary returned by SystemConfiguration can also be set as the value of this property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCFStreamPropertyFTPProxy: CFString
```

## See Also

- [func CFReadStreamCreateForHTTPRequest(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFReadStream>](cfreadstreamcreateforhttprequest(_:_:).md)
  Creates a read stream for a CFHTTP request message.
- [func CFReadStreamCreateForStreamedHTTPRequest(CFAllocator?, CFHTTPMessage, CFReadStream) -> Unmanaged<CFReadStream>](cfreadstreamcreateforstreamedhttprequest(_:_:_:).md)
  Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxy)*