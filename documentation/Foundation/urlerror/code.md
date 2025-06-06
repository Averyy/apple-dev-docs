# URLError.Code

**Framework**: Foundation  
**Kind**: struct

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
struct Code
```

## Topics

### Error codes
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
- [static var cannotMoveFile: URLError.Code](urlerror/code/cannotmovefile.md)
  A download task was unable to move a downloaded file on disk.
- [static var cannotOpenFile: URLError.Code](urlerror/code/cannotopenfile.md)
  A download task was unable to open the downloaded file on disk.
- [static var cannotParseResponse: URLError.Code](urlerror/code/cannotparseresponse.md)
  A task could not parse a response.
- [static var cannotRemoveFile: URLError.Code](urlerror/code/cannotremovefile.md)
  A download task was unable to remove a downloaded file from disk.
- [static var cannotWriteToFile: URLError.Code](urlerror/code/cannotwritetofile.md)
  A download task was unable to write to the downloaded file on disk.
- [static var clientCertificateRejected: URLError.Code](urlerror/code/clientcertificaterejected.md)
  A server certificate was rejected.
- [static var clientCertificateRequired: URLError.Code](urlerror/code/clientcertificaterequired.md)
  A client certificate was required to authenticate an SSL connection during a request.
- [static var dataLengthExceedsMaximum: URLError.Code](urlerror/code/datalengthexceedsmaximum.md)
  The length of the resource data exceeds the maximum allowed.
- [static var dataNotAllowed: URLError.Code](urlerror/code/datanotallowed.md)
  The cellular network disallowed a connection.
- [static var dnsLookupFailed: URLError.Code](urlerror/code/dnslookupfailed.md)
  The host address could not be found via DNS lookup.
- [static var downloadDecodingFailedMidStream: URLError.Code](urlerror/code/downloaddecodingfailedmidstream.md)
  A download task failed to decode an encoded file during the download.
- [static var downloadDecodingFailedToComplete: URLError.Code](urlerror/code/downloaddecodingfailedtocomplete.md)
  A download task failed to decode an encoded file after downloading.
- [static var fileDoesNotExist: URLError.Code](urlerror/code/filedoesnotexist.md)
  A file does not exist.
- [static var fileIsDirectory: URLError.Code](urlerror/code/fileisdirectory.md)
  A request for an FTP file resulted in the server responding that the file is not a plain file, but a directory.
- [static var httpTooManyRedirects: URLError.Code](urlerror/code/httptoomanyredirects.md)
  A redirect loop has been detected or the threshold for number of allowable redirects has been exceeded (currently 16).
- [static var internationalRoamingOff: URLError.Code](urlerror/code/internationalroamingoff.md)
  The attempted connection required activating a data context while roaming, but international roaming is disabled.
- [static var networkConnectionLost: URLError.Code](urlerror/code/networkconnectionlost.md)
  A client or server connection was severed in the middle of an in-progress load.
- [static var noPermissionsToReadFile: URLError.Code](urlerror/code/nopermissionstoreadfile.md)
  A resource couldn’t be read because of insufficient permissions.
- [static var notConnectedToInternet: URLError.Code](urlerror/code/notconnectedtointernet.md)
  A network resource was requested, but an internet connection has not been established and cannot be established automatically.
- [static var redirectToNonExistentLocation: URLError.Code](urlerror/code/redirecttononexistentlocation.md)
  A redirect was specified by way of server response code, but the server did not accompany this code with a redirect URL.
- [static var requestBodyStreamExhausted: URLError.Code](urlerror/code/requestbodystreamexhausted.md)
  A body stream is needed but the client did not provide one.
- [static var resourceUnavailable: URLError.Code](urlerror/code/resourceunavailable.md)
  A requested resource couldn’t be retrieved.
- [static var secureConnectionFailed: URLError.Code](urlerror/code/secureconnectionfailed.md)
  An attempt to establish a secure connection failed for reasons that can’t be expressed more specifically.
- [static var serverCertificateHasBadDate: URLError.Code](urlerror/code/servercertificatehasbaddate.md)
  A server certificate had a date which indicates it has expired, or is not yet valid.
- [static var serverCertificateHasUnknownRoot: URLError.Code](urlerror/code/servercertificatehasunknownroot.md)
  A server certificate was not signed by any root server.
- [static var serverCertificateNotYetValid: URLError.Code](urlerror/code/servercertificatenotyetvalid.md)
  A server certificate is not yet valid.
- [static var serverCertificateUntrusted: URLError.Code](urlerror/code/servercertificateuntrusted.md)
  A server certificate was signed by a root server that isn’t trusted.
- [static var timedOut: URLError.Code](urlerror/code/timedout.md)
  An asynchronous operation timed out.
- [static var unknown: URLError.Code](urlerror/code/unknown.md)
  The URL Loading System encountered an error that it can’t interpret.
- [static var unsupportedURL: URLError.Code](urlerror/code/unsupportedurl.md)
  A properly formed URL couldn’t be handled by the framework.
- [static var userAuthenticationRequired: URLError.Code](urlerror/code/userauthenticationrequired.md)
  Authentication is required to access a resource.
- [static var userCancelledAuthentication: URLError.Code](urlerror/code/usercancelledauthentication.md)
  An asynchronous request for authentication has been canceled by the user.
- [static var zeroByteResource: URLError.Code](urlerror/code/zerobyteresource.md)
  A server reported that a URL has a non-zero content length, but terminated the network connection gracefully without sending any data.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var appTransportSecurityRequiresSecureConnection: URLError.Code](urlerror/apptransportsecurityrequiressecureconnection.md)
  App Transport Security disallowed a connection because there is no secure network connection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/code)*