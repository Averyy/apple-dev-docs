# CFWriteStreamCreateWithFTPURL(_:_:)

**Framework**: CFNetwork  
**Kind**: func

Creates an FTP write stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFWriteStreamCreateWithFTPURL(_ alloc: CFAllocator?, _ ftpURL: CFURL) -> Unmanaged<CFWriteStream>
```

#### Return Value

A new write stream, or `NULL` if the call failed. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates an FTP write stream for uploading data to an FTP URL. If the `ftpURL` parameter is created with the user name and password as part of the URL (such as `ftp://username:password@ftp.example.com`) then the user name and password will automatically be set in the `CFWriteStream`. Call [`CFWriteStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStreamSetProperty(_:_:_:)) to set the steam’s properties, such as `kCFStreamPropertyFTPUserName` and `kCFStreamPropertyFTPPassword` to associate a user name and password with the stream that are used to log in when the stream is opened. See `Constants` for a description of all FTP stream properties.

After creating the write stream, you can call [`CFWriteStreamGetStatus(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStreamGetStatus(_:)) at any time to check the status of the stream.

To initiate a connection with the FTP server, call [`CFWriteStreamOpen(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStreamOpen(_:)). If the URL specifies a directory, the open is immediately followed by the event `kCFStreamEventEndEncountered` (and the stream passes to the state `kCFStreamStatusAtEnd`). Once the stream reaches this state, the directory has been created. Intermediary directories are not created.

To write to the FTP stream, call [`CFWriteStreamWrite(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStreamWrite(_:_:_:)).

To close a connection with the FTP server, call [`CFWriteStreamClose(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStreamClose(_:)).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `ftpURL`: A pointer to a CFURL structure for the URL to be uploaded created by calling any of the   functions, such as  .

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
- [func CFReadStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFReadStream>](cfreadstreamcreatewithftpurl(_:_:).md)
  Creates an FTP read stream.
- [let kCFStreamPropertyFTPAttemptPersistentConnection: CFString](kcfstreampropertyftpattemptpersistentconnection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfwritestreamcreatewithftpurl(_:_:))*