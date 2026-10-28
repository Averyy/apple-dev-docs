# CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Creates readable and writable streams connected to a given `CFHost` object.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.3+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network framework instead

## Declaration

```swift
func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)
```

```c
extern void CFStreamCreatePairWithSocketToCFHost(CFAllocatorRef alloc, CFHostRef host, SInt32 port, CFReadStreamRef*readStream, CFWriteStreamRef*writeStream);
```

## Discussion

The streams do not create a socket or connect to the specified host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## Parameters

- `alloc`: The allocator to use to allocate memory for the `CFReadStream` and `CFWriteStream` objects. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `host`: A `CFHost` object to which the streams are connected.  If unresolved, the host will be resolved prior to connecting.
- `port`: The TCP port number to which the socket streams should connect.
- `readStream`: Upon return, contains a `CFReadStream` object connected to the host `host` on port `port`, or `NULL` if there is a failure during creation. If you pass `NULL`, the function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
- `writeStream`: Upon return, contains a `CFWriteStream` object connected to the host `host` on port `port`, or `NULL` if there is a failure during creation. If you pass `NULL`, the function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Streams
- [func CFReadStreamCreateForHTTPRequest(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFReadStream>](./cfreadstreamcreateforhttprequest%28_,_%29.md)
  Creates a read stream for a CFHTTP request message.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfstreamcreatepairwithsockettocfhost(_:_:_:_:_:))*