# CFStreamErrorHTTP

**Framework**: CFNetwork  
**Kind**: enum

Error codes that a read stream for an HTTP request may return.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum CFStreamErrorHTTP
```

## Topics

### Constants
- [CFStreamErrorHTTP.parseFailure](cfstreamerrorhttp/parsefailure.md)
  A parsing error occurred while an incoming message was being deserialized and appended to a message object. The headers of the incoming message may be formatted improperly.
- [CFStreamErrorHTTP.redirectionLoop](cfstreamerrorhttp/redirectionloop.md)
  A redirection loop has been detected.
- [CFStreamErrorHTTP.badURL](cfstreamerrorhttp/badurl.md)
  The URL is not properly formatted.
### Initializers
- [init?(rawValue: Int32)](cfstreamerrorhttp/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp)*