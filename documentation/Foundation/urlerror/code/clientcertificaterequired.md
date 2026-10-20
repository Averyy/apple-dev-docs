# clientCertificateRequired

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A client certificate was required to authenticate an SSL connection during a request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var clientCertificateRequired: URLError.Code { get }
```

## See Also

### Error codes
- [static var appTransportSecurityRequiresSecureConnection: URLError.Code](./apptransportsecurityrequiressecureconnection.md)
  App Transport Security disallowed a connection because there is no secure network connection.
- [static var backgroundSessionInUseByAnotherProcess: URLError.Code](./backgroundsessioninusebyanotherprocess.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [static var backgroundSessionRequiresSharedContainer: URLError.Code](./backgroundsessionrequiressharedcontainer.md)
  The shared container identifier of the URL session configuration is needed but has not been set.
- [static var backgroundSessionWasDisconnected: URLError.Code](./backgroundsessionwasdisconnected.md)
  The app is suspended or exits while a background data task is processing.
- [static var badServerResponse: URLError.Code](./badserverresponse.md)
  The URL Loading system received bad data from the server.
- [static var badURL: URLError.Code](./badurl.md)
  A malformed URL prevented a URL request from being initiated.
- [static var callIsActive: URLError.Code](./callisactive.md)
  A connection was attempted while a phone call is active on a network that does not support simultaneous phone and data communication (EDGE or GPRS).
- [static var cancelled: URLError.Code](./cancelled.md)
  An asynchronous load has been canceled.
- [static var cannotCloseFile: URLError.Code](./cannotclosefile.md)
  A download task couldn’t close the downloaded file on disk.
- [static var cannotConnectToHost: URLError.Code](./cannotconnecttohost.md)
  An attempt to connect to a host failed.
- [static var cannotCreateFile: URLError.Code](./cannotcreatefile.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [static var cannotDecodeContentData: URLError.Code](./cannotdecodecontentdata.md)
  Content data received during a connection request had an unknown content encoding.
- [static var cannotDecodeRawData: URLError.Code](./cannotdecoderawdata.md)
  Content data received during a connection request could not be decoded for a known content encoding.
- [static var cannotFindHost: URLError.Code](./cannotfindhost.md)
  The host name for a URL could not be resolved.
- [static var cannotLoadFromNetwork: URLError.Code](./cannotloadfromnetwork.md)
  A request to load an item only from the cache could not be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/code/clientcertificaterequired)*