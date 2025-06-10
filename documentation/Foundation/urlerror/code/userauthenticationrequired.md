# userAuthenticationRequired

**Framework**: Foundation  
**Kind**: property

Authentication is required to access a resource.

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
static var userAuthenticationRequired: URLError.Code { get }
```

## See Also

- [static var appTransportSecurityRequiresSecureConnection: URLError.Code](urlerror/code/apptransportsecurityrequiressecureconnection.md)
  App Transport Security disallowed a connection because there is no secure network connection.
- [static var backgroundSessionInUseByAnotherProcess: URLError.Code](urlerror/code/backgroundsessioninusebyanotherprocess.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [static var backgroundSessionRequiresSharedContainer: URLError.Code](urlerror/code/backgroundsessionrequiressharedcontainer.md)
  The shared container identifier of the URL session configuration is needed but has not been set.
- [static var backgroundSessionWasDisconnected: URLError.Code](urlerror/code/backgroundsessionwasdisconnected.md)
  The app is suspended or exits while a background data task is processing.
- [static var badServerResponse: URLError.Code](urlerror/code/badserverresponse.md)
  The URL Loading system received bad data from the server.
- [static var badURL: URLError.Code](urlerror/code/badurl.md)
  A malformed URL prevented a URL request from being initiated.
- [static var callIsActive: URLError.Code](urlerror/code/callisactive.md)
  A connection was attempted while a phone call is active on a network that does not support simultaneous phone and data communication (EDGE or GPRS).
- [static var cancelled: URLError.Code](urlerror/code/cancelled.md)
  An asynchronous load has been canceled.
- [static var cannotCloseFile: URLError.Code](urlerror/code/cannotclosefile.md)
  A download task couldn’t close the downloaded file on disk.
- [static var cannotConnectToHost: URLError.Code](urlerror/code/cannotconnecttohost.md)
  An attempt to connect to a host failed.
- [static var cannotCreateFile: URLError.Code](urlerror/code/cannotcreatefile.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [static var cannotDecodeContentData: URLError.Code](urlerror/code/cannotdecodecontentdata.md)
  Content data received during a connection request had an unknown content encoding.
- [static var cannotDecodeRawData: URLError.Code](urlerror/code/cannotdecoderawdata.md)
  Content data received during a connection request could not be decoded for a known content encoding.
- [static var cannotFindHost: URLError.Code](urlerror/code/cannotfindhost.md)
  The host name for a URL could not be resolved.
- [static var cannotLoadFromNetwork: URLError.Code](urlerror/code/cannotloadfromnetwork.md)
  A request to load an item only from the cache could not be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/code/userauthenticationrequired)*