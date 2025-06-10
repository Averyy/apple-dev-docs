# NSURLErrorFileOutsideSafeArea

**Framework**: Foundation  
**Kind**: var

An internal file operation failed.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var NSURLErrorFileOutsideSafeArea: Int { get }
```

#### Discussion

This error is never sent to third-party apps.

## See Also

- [var NSURLErrorAppTransportSecurityRequiresSecureConnection: Int](nsurlerrorapptransportsecurityrequiressecureconnection-swift.var.md)
  App Transport Security disallowed a connection because there is no secure network connection.
- [var NSURLErrorBackgroundSessionInUseByAnotherProcess: Int](nsurlerrorbackgroundsessioninusebyanotherprocess-swift.var.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [var NSURLErrorBackgroundSessionRequiresSharedContainer: Int](nsurlerrorbackgroundsessionrequiressharedcontainer-swift.var.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [var NSURLErrorBackgroundSessionWasDisconnected: Int](nsurlerrorbackgroundsessionwasdisconnected-swift.var.md)
  The app is suspended or exits while a background data task is processing.
- [var NSURLErrorBadServerResponse: Int](nsurlerrorbadserverresponse-swift.var.md)
  The URL Loading System received bad data from the server.
- [var NSURLErrorBadURL: Int](nsurlerrorbadurl-swift.var.md)
  A malformed URL prevented a URL request from being initiated.
- [var NSURLErrorCallIsActive: Int](nsurlerrorcallisactive-swift.var.md)
  A connection was attempted while a phone call was active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [var NSURLErrorCancelled: Int](nsurlerrorcancelled-swift.var.md)
  An asynchronous load has been canceled.
- [var NSURLErrorCannotCloseFile: Int](nsurlerrorcannotclosefile-swift.var.md)
  A download task couldn’t close the downloaded file on disk.
- [var NSURLErrorCannotConnectToHost: Int](nsurlerrorcannotconnecttohost-swift.var.md)
  An attempt to connect to a host failed.
- [var NSURLErrorCannotCreateFile: Int](nsurlerrorcannotcreatefile-swift.var.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [var NSURLErrorCannotDecodeContentData: Int](nsurlerrorcannotdecodecontentdata-swift.var.md)
  Content data received during a connection request had an unknown content encoding.
- [var NSURLErrorCannotDecodeRawData: Int](nsurlerrorcannotdecoderawdata-swift.var.md)
  Content data received during a connection request couldn’t be decoded for a known content encoding.
- [var NSURLErrorCannotFindHost: Int](nsurlerrorcannotfindhost-swift.var.md)
  The host name for a URL couldn’t be resolved.
- [var NSURLErrorCannotLoadFromNetwork: Int](nsurlerrorcannotloadfromnetwork-swift.var.md)
  A specific request to load an item only from the cache couldn’t be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlerrorfileoutsidesafearea-swift.var)*