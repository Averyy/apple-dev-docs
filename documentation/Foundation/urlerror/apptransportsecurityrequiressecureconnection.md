# appTransportSecurityRequiresSecureConnection

**Framework**: Foundation  
**Kind**: property

App Transport Security disallowed a connection because there is no secure network connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var appTransportSecurityRequiresSecureConnection: URLError.Code { get }
```

#### Discussion

Starting in iOS 9.0 and macOS v10.11, App Transport Security (ATS) is enabled by default for connections created by [`URLSession`](urlsession.md). ATS requires the use of best practice secure protocols in HTTPS. For more information on ATS, see [`NSAppTransportSecurity`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSAppTransportSecurity) in  [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

- [static var backgroundSessionInUseByAnotherProcess: URLError.Code](urlerror/backgroundsessioninusebyanotherprocess.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [static var backgroundSessionRequiresSharedContainer: URLError.Code](urlerror/backgroundsessionrequiressharedcontainer.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [static var backgroundSessionWasDisconnected: URLError.Code](urlerror/backgroundsessionwasdisconnected.md)
  The app is suspended or exits while a background data task is processing.
- [static var badServerResponse: URLError.Code](urlerror/badserverresponse.md)
  The URL Loading System received bad data from the server.
- [static var badURL: URLError.Code](urlerror/badurl.md)
  A malformed URL prevented a URL request from being initiated.
- [static var callIsActive: URLError.Code](urlerror/callisactive.md)
  A connection was attempted while a phone call is active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [static var cancelled: URLError.Code](urlerror/cancelled.md)
  An asynchronous load has been canceled.
- [static var cannotCloseFile: URLError.Code](urlerror/cannotclosefile.md)
  A download task couldn’t close the downloaded file on disk.
- [static var cannotConnectToHost: URLError.Code](urlerror/cannotconnecttohost.md)
  An attempt to connect to a host failed.
- [static var cannotCreateFile: URLError.Code](urlerror/cannotcreatefile.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [static var cannotDecodeContentData: URLError.Code](urlerror/cannotdecodecontentdata.md)
  Content data received during a connection request had an unknown content encoding.
- [static var cannotDecodeRawData: URLError.Code](urlerror/cannotdecoderawdata.md)
  Content data received during a connection request couldn’t be decoded for a known content encoding.
- [static var cannotFindHost: URLError.Code](urlerror/cannotfindhost.md)
  The host name for a URL couldn’t be resolved.
- [static var cannotLoadFromNetwork: URLError.Code](urlerror/cannotloadfromnetwork.md)
  A request to load an item only from the cache could not be satisfied.
- [static var cannotMoveFile: URLError.Code](urlerror/cannotmovefile.md)
  A download task was unable to move a downloaded file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/apptransportsecurityrequiressecureconnection)*