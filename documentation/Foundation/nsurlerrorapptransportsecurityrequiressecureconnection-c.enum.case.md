# NSURLErrorAppTransportSecurityRequiresSecureConnection

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

App Transport Security disallowed a connection because there is no secure network connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
NSURLErrorAppTransportSecurityRequiresSecureConnection
```

#### Discussion

Starting in iOS 9.0 and macOS v10.11, App Transport Security (ATS) is enabled by default for connections created by [`URLSession`](./urlsession.md). ATS requires the use of best practice secure protocols in HTTPS. For more information on ATS, see [NSAppTransportSecurity](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSAppTransportSecurity) in [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

### URL Errors
- [NSURLErrorBackgroundSessionInUseByAnotherProcess](./nsurlerrorbackgroundsessioninusebyanotherprocess-c.enum.case.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [NSURLErrorBackgroundSessionRequiresSharedContainer](./nsurlerrorbackgroundsessionrequiressharedcontainer-c.enum.case.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [NSURLErrorBackgroundSessionWasDisconnected](./nsurlerrorbackgroundsessionwasdisconnected-c.enum.case.md)
  The app is suspended or exits while a background data task is processing.
- [NSURLErrorBadServerResponse](./nsurlerrorbadserverresponse-c.enum.case.md)
  The URL Loading System received bad data from the server.
- [NSURLErrorBadURL](./nsurlerrorbadurl-c.enum.case.md)
  A malformed URL prevented a URL request from being initiated.
- [NSURLErrorCallIsActive](./nsurlerrorcallisactive-c.enum.case.md)
  A connection was attempted while a phone call was active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [NSURLErrorCancelled](./nsurlerrorcancelled-c.enum.case.md)
  An asynchronous load has been canceled.
- [NSURLErrorCannotCloseFile](./nsurlerrorcannotclosefile-c.enum.case.md)
  A download task couldn’t close the downloaded file on disk.
- [NSURLErrorCannotConnectToHost](./nsurlerrorcannotconnecttohost-c.enum.case.md)
  An attempt to connect to a host failed.
- [NSURLErrorCannotCreateFile](./nsurlerrorcannotcreatefile-c.enum.case.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [NSURLErrorCannotDecodeContentData](./nsurlerrorcannotdecodecontentdata-c.enum.case.md)
  Content data received during a connection request had an unknown content encoding.
- [NSURLErrorCannotDecodeRawData](./nsurlerrorcannotdecoderawdata-c.enum.case.md)
  Content data received during a connection request couldn’t be decoded for a known content encoding.
- [NSURLErrorCannotFindHost](./nsurlerrorcannotfindhost-c.enum.case.md)
  The host name for a URL couldn’t be resolved.
- [NSURLErrorCannotLoadFromNetwork](./nsurlerrorcannotloadfromnetwork-c.enum.case.md)
  A specific request to load an item only from the cache couldn’t be satisfied.
- [NSURLErrorCannotMoveFile](./nsurlerrorcannotmovefile-c.enum.case.md)
  A downloaded file on disk couldn’t be moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorapptransportsecurityrequiressecureconnection-c.enum.case)*