# CFReadStreamCreateForHTTPRequest(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Creates a read stream for a CFHTTP request message.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use NSURLSession API for http requests

## Declaration

```swift
func CFReadStreamCreateForHTTPRequest(_ alloc: CFAllocator?, _ request: CFHTTPMessage) -> Unmanaged<CFReadStream>
```

```c
extern CFReadStreamRefCFReadStreamCreateForHTTPRequest(CFAllocatorRef alloc, CFHTTPMessageRef request);
```

## Return Value

A new read stream, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function creates a read stream and associates it with the specified request. Automatic redirection is disabled by default. After creating the read stream, you can call [`CFReadStreamGetError(_:)`](../CoreFoundation/cfreadstreamgeterror%28_%29.md) at any time to check the status of the stream. You may want to call `CFHTTPReadStreamSetRedirectsAutomatically` to enable automatic redirection, or `CFHTTPReadStreamSetProxy` to set the name and port number for a proxy. To serialize the request and send it, call [`CFReadStreamOpen(_:)`](../CoreFoundation/cfreadstreamopen%28_%29.md).

If the body of the request is too long to keep in memory, call [`CFReadStreamCreateForStreamedHTTPRequest(_:_:_:)`](./cfreadstreamcreateforstreamedhttprequest%28_,_,_%29.md) instead of this function.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `request`: A CFHTTP request message whose body and headers have been set.

## See Also

### Streams
- [func CFReadStreamCreateForStreamedHTTPRequest(CFAllocator?, CFHTTPMessage, CFReadStream) -> Unmanaged<CFReadStream>](./cfreadstreamcreateforstreamedhttprequest%28_,_,_%29.md)
  Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.
- [let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString](./kcfstreampropertyhttpattemptpersistentconnection.md)
- [let kCFStreamPropertyHTTPFinalRequest: CFString](./kcfstreampropertyhttpfinalrequest.md)
  HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set.
- [let kCFStreamPropertyHTTPFinalURL: CFString](./kcfstreampropertyhttpfinalurl.md)
  HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set.
- [let kCFStreamPropertyHTTPProxy: CFString](./kcfstreampropertyhttpproxy.md)
- [let kCFStreamPropertyHTTPProxyHost: CFString](./kcfstreampropertyhttpproxyhost.md)
- [let kCFStreamPropertyHTTPProxyPort: CFString](./kcfstreampropertyhttpproxyport.md)
- [let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString](./kcfstreampropertyhttprequestbyteswrittencount.md)
- [let kCFStreamPropertyHTTPResponseHeader: CFString](./kcfstreampropertyhttpresponseheader.md)
  HTTP Response Header property. When copied by [`CFReadStreamCopyProperty(_:_:)`](../CoreFoundation/cfreadstreamcopyproperty%28_,_%29.md), the header of an HTTP response message is returned.
- [let kCFStreamPropertyHTTPSProxyHost: CFString](./kcfstreampropertyhttpsproxyhost.md)
- [let kCFStreamPropertyHTTPSProxyPort: CFString](./kcfstreampropertyhttpsproxyport.md)
- [let kCFStreamPropertyHTTPShouldAutoredirect: CFString](./kcfstreampropertyhttpshouldautoredirect.md)
  HTTP Should Auto Redirect property. Set this property to `kCFBooleanTrue` to enable autoredirection; set this property to `kCFBooleanFalse` to disable autoredirection.
- [func CFWriteStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFWriteStream>](./cfwritestreamcreatewithftpurl%28_,_%29.md)
  Creates an FTP write stream.
- [func CFReadStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFReadStream>](./cfreadstreamcreatewithftpurl%28_,_%29.md)
  Creates an FTP read stream.
- [let kCFStreamPropertyFTPAttemptPersistentConnection: CFString](./kcfstreampropertyftpattemptpersistentconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfreadstreamcreateforhttprequest(_:_:))*