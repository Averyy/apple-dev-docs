# URLError.Code

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Codes that describe errors within the URL loading API.

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
- [static var appTransportSecurityRequiresSecureConnection: URLError.Code](./code/apptransportsecurityrequiressecureconnection.md)
  App Transport Security disallowed a connection because there is no secure network connection.
- [static var backgroundSessionInUseByAnotherProcess: URLError.Code](./code/backgroundsessioninusebyanotherprocess.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [static var backgroundSessionRequiresSharedContainer: URLError.Code](./code/backgroundsessionrequiressharedcontainer.md)
  The shared container identifier of the URL session configuration is needed but has not been set.
- [static var backgroundSessionWasDisconnected: URLError.Code](./code/backgroundsessionwasdisconnected.md)
  The app is suspended or exits while a background data task is processing.
- [static var badServerResponse: URLError.Code](./code/badserverresponse.md)
  The URL Loading system received bad data from the server.
- [static var badURL: URLError.Code](./code/badurl.md)
  A malformed URL prevented a URL request from being initiated.
- [static var callIsActive: URLError.Code](./code/callisactive.md)
  A connection was attempted while a phone call is active on a network that does not support simultaneous phone and data communication (EDGE or GPRS).
- [static var cancelled: URLError.Code](./code/cancelled.md)
  An asynchronous load has been canceled.
- [static var cannotCloseFile: URLError.Code](./code/cannotclosefile.md)
  A download task couldn’t close the downloaded file on disk.
- [static var cannotConnectToHost: URLError.Code](./code/cannotconnecttohost.md)
  An attempt to connect to a host failed.
- [static var cannotCreateFile: URLError.Code](./code/cannotcreatefile.md)
  A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [static var cannotDecodeContentData: URLError.Code](./code/cannotdecodecontentdata.md)
  Content data received during a connection request had an unknown content encoding.
- [static var cannotDecodeRawData: URLError.Code](./code/cannotdecoderawdata.md)
  Content data received during a connection request could not be decoded for a known content encoding.
- [static var cannotFindHost: URLError.Code](./code/cannotfindhost.md)
  The host name for a URL could not be resolved.
- [static var cannotLoadFromNetwork: URLError.Code](./code/cannotloadfromnetwork.md)
  A request to load an item only from the cache could not be satisfied.
- [static var cannotMoveFile: URLError.Code](./code/cannotmovefile.md)
  A download task was unable to move a downloaded file on disk.
- [static var cannotOpenFile: URLError.Code](./code/cannotopenfile.md)
  A download task was unable to open the downloaded file on disk.
- [static var cannotParseResponse: URLError.Code](./code/cannotparseresponse.md)
  A task could not parse a response.
- [static var cannotRemoveFile: URLError.Code](./code/cannotremovefile.md)
  A download task was unable to remove a downloaded file from disk.
- [static var cannotWriteToFile: URLError.Code](./code/cannotwritetofile.md)
  A download task was unable to write to the downloaded file on disk.
- [static var clientCertificateRejected: URLError.Code](./code/clientcertificaterejected.md)
  A server certificate was rejected.
- [static var clientCertificateRequired: URLError.Code](./code/clientcertificaterequired.md)
  A client certificate was required to authenticate an SSL connection during a request.
- [static var dataLengthExceedsMaximum: URLError.Code](./code/datalengthexceedsmaximum.md)
  The length of the resource data exceeds the maximum allowed.
- [static var dataNotAllowed: URLError.Code](./code/datanotallowed.md)
  The cellular network disallowed a connection.
- [static var dnsLookupFailed: URLError.Code](./code/dnslookupfailed.md)
  The host address could not be found via DNS lookup.
- [static var downloadDecodingFailedMidStream: URLError.Code](./code/downloaddecodingfailedmidstream.md)
  A download task failed to decode an encoded file during the download.
- [static var downloadDecodingFailedToComplete: URLError.Code](./code/downloaddecodingfailedtocomplete.md)
  A download task failed to decode an encoded file after downloading.
- [static var fileDoesNotExist: URLError.Code](./code/filedoesnotexist.md)
  A file does not exist.
- [static var fileIsDirectory: URLError.Code](./code/fileisdirectory.md)
  A request for an FTP file resulted in the server responding that the file is not a plain file, but a directory.
- [static var httpTooManyRedirects: URLError.Code](./code/httptoomanyredirects.md)
  A redirect loop has been detected or the threshold for number of allowable redirects has been exceeded (currently 16).
- [static var internationalRoamingOff: URLError.Code](./code/internationalroamingoff.md)
  The attempted connection required activating a data context while roaming, but international roaming is disabled.
- [static var networkConnectionLost: URLError.Code](./code/networkconnectionlost.md)
  A client or server connection was severed in the middle of an in-progress load.
- [static var noPermissionsToReadFile: URLError.Code](./code/nopermissionstoreadfile.md)
  A resource couldn’t be read because of insufficient permissions.
- [static var notConnectedToInternet: URLError.Code](./code/notconnectedtointernet.md)
  A network resource was requested, but an internet connection has not been established and cannot be established automatically.
- [static var redirectToNonExistentLocation: URLError.Code](./code/redirecttononexistentlocation.md)
  A redirect was specified by way of server response code, but the server did not accompany this code with a redirect URL.
- [static var requestBodyStreamExhausted: URLError.Code](./code/requestbodystreamexhausted.md)
  A body stream is needed but the client did not provide one.
- [static var resourceUnavailable: URLError.Code](./code/resourceunavailable.md)
  A requested resource couldn’t be retrieved.
- [static var secureConnectionFailed: URLError.Code](./code/secureconnectionfailed.md)
  An attempt to establish a secure connection failed for reasons that can’t be expressed more specifically.
- [static var serverCertificateHasBadDate: URLError.Code](./code/servercertificatehasbaddate.md)
  A server certificate had a date which indicates it has expired, or is not yet valid.
- [static var serverCertificateHasUnknownRoot: URLError.Code](./code/servercertificatehasunknownroot.md)
  A server certificate was not signed by any root server.
- [static var serverCertificateNotYetValid: URLError.Code](./code/servercertificatenotyetvalid.md)
  A server certificate is not yet valid.
- [static var serverCertificateUntrusted: URLError.Code](./code/servercertificateuntrusted.md)
  A server certificate was signed by a root server that isn’t trusted.
- [static var timedOut: URLError.Code](./code/timedout.md)
  An asynchronous operation timed out.
- [static var unknown: URLError.Code](./code/unknown.md)
  The URL Loading System encountered an error that it can’t interpret.
- [static var unsupportedURL: URLError.Code](./code/unsupportedurl.md)
  A properly formed URL couldn’t be handled by the framework.
- [static var userAuthenticationRequired: URLError.Code](./code/userauthenticationrequired.md)
  Authentication is required to access a resource.
- [static var userCancelledAuthentication: URLError.Code](./code/usercancelledauthentication.md)
  An asynchronous request for authentication has been canceled by the user.
- [static var zeroByteResource: URLError.Code](./code/zerobyteresource.md)
  A server reported that a URL has a non-zero content length, but terminated the network connection gracefully without sending any data.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error codes
- [static var appTransportSecurityRequiresSecureConnection: URLError.Code](./apptransportsecurityrequiressecureconnection.md)
  App Transport Security disallowed a connection because there is no secure network connection.
- [static var backgroundSessionInUseByAnotherProcess: URLError.Code](./backgroundsessioninusebyanotherprocess.md)
  An app or app extension attempted to connect to a background session that is already connected to a process.
- [static var backgroundSessionRequiresSharedContainer: URLError.Code](./backgroundsessionrequiressharedcontainer.md)
  The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [static var backgroundSessionWasDisconnected: URLError.Code](./backgroundsessionwasdisconnected.md)
  The app is suspended or exits while a background data task is processing.
- [static var badServerResponse: URLError.Code](./badserverresponse.md)
  The URL Loading System received bad data from the server.
- [static var badURL: URLError.Code](./badurl.md)
  A malformed URL prevented a URL request from being initiated.
- [static var callIsActive: URLError.Code](./callisactive.md)
  A connection was attempted while a phone call is active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
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
  Content data received during a connection request couldn’t be decoded for a known content encoding.
- [static var cannotFindHost: URLError.Code](./cannotfindhost.md)
  The host name for a URL couldn’t be resolved.
- [static var cannotLoadFromNetwork: URLError.Code](./cannotloadfromnetwork.md)
  A request to load an item only from the cache could not be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/code)*