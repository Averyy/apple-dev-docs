# URLError

**Framework**: Foundation  
**Kind**: struct

Error codes returned by URL loading APIs.

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
struct URLError
```

## Mentions

- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)

#### Overview

These error codes are for [`NSError`](nserror.md) objects in the domain [`NSURLErrorDomain`](nsurlerrordomain.md).

## Topics

### Error details
- [var failingURL: URL?](urlerror/failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](urlerror/failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var failureURLString: String?](urlerror/failureurlstring.md)
  The string for the URL which caused a load to fail.
- [var downloadTaskResumeData: Data?](urlerror/downloadtaskresumedata.md)
  An opaque data object used to resume a failed download task.
- [var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason?](urlerror/backgroundtaskcancelledreason-swift.property.md)
  The reason for canceling a background task.
- [URLError.BackgroundTaskCancelledReason](urlerror/backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](urlerror/networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
### Error codes
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
- [static var cannotMoveFile: URLError.Code](urlerror/cannotmovefile.md)
  A download task was unable to move a downloaded file on disk.
- [static var cannotOpenFile: URLError.Code](urlerror/cannotopenfile.md)
  A download task was unable to open the downloaded file on disk.
- [static var cannotParseResponse: URLError.Code](urlerror/cannotparseresponse.md)
  A task couldn’t parse a response.
- [static var cannotRemoveFile: URLError.Code](urlerror/cannotremovefile.md)
  A download task was unable to remove a downloaded file from disk.
- [static var cannotWriteToFile: URLError.Code](urlerror/cannotwritetofile.md)
  A download task was unable to write to the downloaded file on disk.
- [static var clientCertificateRejected: URLError.Code](urlerror/clientcertificaterejected.md)
  A server certificate was rejected.
- [static var clientCertificateRequired: URLError.Code](urlerror/clientcertificaterequired.md)
  A client certificate was required to authenticate an SSL connection during a request.
- [static var dataLengthExceedsMaximum: URLError.Code](urlerror/datalengthexceedsmaximum.md)
  The length of the resource data exceeds the maximum allowed.
- [static var dataNotAllowed: URLError.Code](urlerror/datanotallowed.md)
  The cellular network disallowed a connection.
- [static var dnsLookupFailed: URLError.Code](urlerror/dnslookupfailed.md)
  The host address couldn’t be found via DNS lookup.
- [static var downloadDecodingFailedMidStream: URLError.Code](urlerror/downloaddecodingfailedmidstream.md)
  A download task failed to decode an encoded file during the download.
- [static var downloadDecodingFailedToComplete: URLError.Code](urlerror/downloaddecodingfailedtocomplete.md)
  A download task failed to decode an encoded file after downloading.
- [static var fileDoesNotExist: URLError.Code](urlerror/filedoesnotexist.md)
  The specified file doesn’t exist.
- [static var fileIsDirectory: URLError.Code](urlerror/fileisdirectory.md)
  A request for an FTP file resulted in the server responding that the file is not a plain file, but a directory.
- [static var httpTooManyRedirects: URLError.Code](urlerror/httptoomanyredirects.md)
  A redirect loop has been detected or the threshold for number of allowable redirects has been exceeded (currently 16).
- [static var internationalRoamingOff: URLError.Code](urlerror/internationalroamingoff.md)
  The attempted connection required activating a data context while roaming, but international roaming is disabled.
- [static var networkConnectionLost: URLError.Code](urlerror/networkconnectionlost.md)
  A client or server connection was severed in the middle of an in-progress load.
- [static var noPermissionsToReadFile: URLError.Code](urlerror/nopermissionstoreadfile.md)
  A resource couldn’t be read because of insufficient permissions.
- [static var notConnectedToInternet: URLError.Code](urlerror/notconnectedtointernet.md)
  A network resource was requested, but an internet connection hasn’t been established and can’t be established automatically.
- [static var redirectToNonExistentLocation: URLError.Code](urlerror/redirecttononexistentlocation.md)
  A redirect was specified by way of server response code, but the server didn’t accompany this code with a redirect URL.
- [static var requestBodyStreamExhausted: URLError.Code](urlerror/requestbodystreamexhausted.md)
  A body stream is needed but the client didn’t provide one.
- [static var resourceUnavailable: URLError.Code](urlerror/resourceunavailable.md)
  A requested resource couldn’t be retrieved.
- [static var serverCertificateHasBadDate: URLError.Code](urlerror/servercertificatehasbaddate.md)
  A server certificate is expired, or is not yet valid.
- [static var serverCertificateHasUnknownRoot: URLError.Code](urlerror/servercertificatehasunknownroot.md)
  A server certificate wasn’t signed by any root server.
- [static var serverCertificateNotYetValid: URLError.Code](urlerror/servercertificatenotyetvalid.md)
  A server certificate isn’t valid yet.
- [static var serverCertificateUntrusted: URLError.Code](urlerror/servercertificateuntrusted.md)
  A server certificate was signed by a root server that isn’t trusted.
- [static var secureConnectionFailed: URLError.Code](urlerror/secureconnectionfailed.md)
  An attempt to establish a secure connection failed for reasons that can’t be expressed more specifically.
- [static var timedOut: URLError.Code](urlerror/timedout.md)
  An asynchronous operation timed out.
- [static var unknown: URLError.Code](urlerror/unknown.md)
  The URL Loading System encountered an error that it can’t interpret.
- [static var unsupportedURL: URLError.Code](urlerror/unsupportedurl.md)
  A properly formed URL couldn’t be handled by the framework.
- [static var userAuthenticationRequired: URLError.Code](urlerror/userauthenticationrequired.md)
  Authentication is required to access a resource.
- [static var userCancelledAuthentication: URLError.Code](urlerror/usercancelledauthentication.md)
  An asynchronous request for authentication has been canceled by the user.
- [static var zeroByteResource: URLError.Code](urlerror/zerobyteresource.md)
  A server reported that a URL has a non-zero content length, but terminated the network connection gracefully without sending any data.
- [URLError.Code](urlerror/code.md)
  The error code itself.
### Instance Properties
- [var uploadTaskResumeData: Data?](urlerror/uploadtaskresumedata.md)
  An opaque data blob to resume a failed upload task.

## Relationships

### Conforms To
- [CustomNSError](customnserror.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [URL Loading System error info keys](url-loading-system-error-info-keys.md)
  Recognize these keys from the user info dictionary of error objects produced by URL Loading APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror)*