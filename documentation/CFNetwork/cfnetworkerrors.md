# CFNetworkErrors

**Framework**: CFNetwork  
**Kind**: enum

This enumeration contains error codes returned under the error domain [`kCFErrorDomainCFNetwork`](kcferrordomaincfnetwork.md).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum CFNetworkErrors
```

#### Overview

To determine the source of an error, examine the `userInfo` dictionary included in the `CFError` object returned by a function call or call [`CFErrorGetDomain(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFErrorGetDomain(_:)) and pass in the `CFError` object and the domain whose value you want to read. These errors are all part of the `kCFErrorDomainCFNetwork` domain.

## Topics

### Constants
- [CFNetworkErrors.cfHostErrorHostNotFound](cfnetworkerrors/cfhosterrorhostnotfound.md)
  The specified host wasn’t found.
- [CFNetworkErrors.cfHostErrorUnknown](cfnetworkerrors/cfhosterrorunknown.md)
  An unknown error.
- [CFNetworkErrors.cfsocksErrorUnknownClientVersion](cfnetworkerrors/cfsockserrorunknownclientversion.md)
  The SOCKS server rejected access because it doesn’t support connections with the requested SOCKS version.
- [CFNetworkErrors.cfsocksErrorUnsupportedServerVersion](cfnetworkerrors/cfsockserrorunsupportedserverversion.md)
  The SOCKS server doesn’t support the requested version.
- [CFNetworkErrors.cfsocks4ErrorRequestFailed](cfnetworkerrors/cfsocks4errorrequestfailed.md)
  The server rejected the request, or the request failed.
- [CFNetworkErrors.cfsocks4ErrorIdentdFailed](cfnetworkerrors/cfsocks4erroridentdfailed.md)
  The server couldn’t connect to the `identd` daemon on the client and rejected the request.
- [CFNetworkErrors.cfsocks4ErrorIdConflict](cfnetworkerrors/cfsocks4erroridconflict.md)
  The server rejected the request because the client program and the `identd` daemon reported different user IDs.
- [CFNetworkErrors.cfsocks4ErrorUnknownStatusCode](cfnetworkerrors/cfsocks4errorunknownstatuscode.md)
  The server returned an unknown status code.
- [CFNetworkErrors.cfsocks5ErrorBadState](cfnetworkerrors/cfsocks5errorbadstate.md)
  The stream isn’t in a state that allows the requested operation.
- [CFNetworkErrors.cfsocks5ErrorBadResponseAddr](cfnetworkerrors/cfsocks5errorbadresponseaddr.md)
  The address type returned isn’t supported.
- [CFNetworkErrors.cfsocks5ErrorBadCredentials](cfnetworkerrors/cfsocks5errorbadcredentials.md)
  The SOCKS server refused the client connection because of bad login credentials.
- [CFNetworkErrors.cfsocks5ErrorUnsupportedNegotiationMethod](cfnetworkerrors/cfsocks5errorunsupportednegotiationmethod.md)
  The requested method isn’t supported.
- [CFNetworkErrors.cfsocks5ErrorNoAcceptableMethod](cfnetworkerrors/cfsocks5errornoacceptablemethod.md)
  The client and server couldn’t find a mutually agreeable authentication method.
- [CFNetworkErrors.cfftpErrorUnexpectedStatusCode](cfnetworkerrors/cfftperrorunexpectedstatuscode.md)
  The server returned an unexpected status code.
- [CFNetworkErrors.cfErrorHTTPAuthenticationTypeUnsupported](cfnetworkerrors/cferrorhttpauthenticationtypeunsupported.md)
  The client and server couldn’t agree on a supported authentication type.
- [CFNetworkErrors.cfErrorHTTPBadCredentials](cfnetworkerrors/cferrorhttpbadcredentials.md)
  The server rejected the credentials provided for an authenticated connection.
- [CFNetworkErrors.cfErrorHTTPConnectionLost](cfnetworkerrors/cferrorhttpconnectionlost.md)
  The connection to the server was dropped.
- [CFNetworkErrors.cfErrorHTTPParseFailure](cfnetworkerrors/cferrorhttpparsefailure.md)
  The HTTP server response couldn’t be parsed.
- [CFNetworkErrors.cfErrorHTTPRedirectionLoopDetected](cfnetworkerrors/cferrorhttpredirectionloopdetected.md)
  Too many HTTP redirects occurred before reaching a page that didn’t redirect the client to another page.
- [CFNetworkErrors.cfErrorHTTPBadURL](cfnetworkerrors/cferrorhttpbadurl.md)
  The requested URL couldn’t be retrieved.
- [CFNetworkErrors.cfErrorHTTPProxyConnectionFailure](cfnetworkerrors/cferrorhttpproxyconnectionfailure.md)
  A connection to the HTTPS proxy couldn’t be established.
- [CFNetworkErrors.cfErrorHTTPBadProxyCredentials](cfnetworkerrors/cferrorhttpbadproxycredentials.md)
  The proxy rejected the authentication credentials provided for logging in.
- [CFNetworkErrors.cfErrorPACFileError](cfnetworkerrors/cferrorpacfileerror.md)
  An error occurred with the proxy autoconfiguration file.
- [CFNetworkErrors.cfErrorPACFileAuth](cfnetworkerrors/cferrorpacfileauth.md)
  The authentication credentials provided by the proxy autoconfiguration file were rejected.
- [CFNetworkErrors.cfErrorHTTPSProxyConnectionFailure](cfnetworkerrors/cferrorhttpsproxyconnectionfailure.md)
  A connection couldn’t be established to the HTTPS proxy.
- [CFNetworkErrors.cfStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod](cfnetworkerrors/cfstreamerrorhttpsproxyfailureunexpectedresponsetoconnectmethod.md)
  The HTTPS proxy returned an unexpected status code, such as a `3xx` redirect.
- [CFNetworkErrors.cfurlErrorUnknown](cfnetworkerrors/cfurlerrorunknown.md)
  An unknown error occurred.
- [CFNetworkErrors.cfurlErrorCancelled](cfnetworkerrors/cfurlerrorcancelled.md)
  The connection was cancelled.
- [CFNetworkErrors.cfurlErrorBadURL](cfnetworkerrors/cfurlerrorbadurl.md)
  The connection failed due to a malformed URL.
- [CFNetworkErrors.cfurlErrorTimedOut](cfnetworkerrors/cfurlerrortimedout.md)
  The connection timed out.
- [CFNetworkErrors.cfurlErrorUnsupportedURL](cfnetworkerrors/cfurlerrorunsupportedurl.md)
  The connection failed due to an unsupported URL scheme.
- [CFNetworkErrors.cfurlErrorCannotFindHost](cfnetworkerrors/cfurlerrorcannotfindhost.md)
  The connection failed because the host couldn’t be found.
- [CFNetworkErrors.cfurlErrorCannotConnectToHost](cfnetworkerrors/cfurlerrorcannotconnecttohost.md)
  The connection failed because a connection can’t be made to the host.
- [CFNetworkErrors.cfurlErrorNetworkConnectionLost](cfnetworkerrors/cfurlerrornetworkconnectionlost.md)
  The connection failed because the network connection was lost.
- [CFNetworkErrors.cfurlErrorDNSLookupFailed](cfnetworkerrors/cfurlerrordnslookupfailed.md)
  The connection failed because the DNS lookup failed.
- [CFNetworkErrors.cfurlErrorHTTPTooManyRedirects](cfnetworkerrors/cfurlerrorhttptoomanyredirects.md)
  The HTTP connection failed due to too many redirects.
- [CFNetworkErrors.cfurlErrorResourceUnavailable](cfnetworkerrors/cfurlerrorresourceunavailable.md)
  The connection’s resource is unavailable.
- [CFNetworkErrors.cfurlErrorNotConnectedToInternet](cfnetworkerrors/cfurlerrornotconnectedtointernet.md)
  The connection failed because the device isn’t connected to the internet.
- [CFNetworkErrors.cfurlErrorRedirectToNonExistentLocation](cfnetworkerrors/cfurlerrorredirecttononexistentlocation.md)
  The connection was redirected to a nonexistent location.
- [CFNetworkErrors.cfurlErrorBadServerResponse](cfnetworkerrors/cfurlerrorbadserverresponse.md)
  The connection received an invalid server response.
- [CFNetworkErrors.cfurlErrorUserCancelledAuthentication](cfnetworkerrors/cfurlerrorusercancelledauthentication.md)
  The connection failed because the user cancelled required authentication.
- [CFNetworkErrors.cfurlErrorUserAuthenticationRequired](cfnetworkerrors/cfurlerroruserauthenticationrequired.md)
  The connection failed because it requires authentication.
- [CFNetworkErrors.cfurlErrorZeroByteResource](cfnetworkerrors/cfurlerrorzerobyteresource.md)
  The resource retrieved by the connection is zero bytes.
- [CFNetworkErrors.cfurlErrorCannotDecodeRawData](cfnetworkerrors/cfurlerrorcannotdecoderawdata.md)
  The connection can’t decode data encoded with a known content encoding.
- [CFNetworkErrors.cfurlErrorCannotDecodeContentData](cfnetworkerrors/cfurlerrorcannotdecodecontentdata.md)
  The connection can’t decode data encoded with an unknown content encoding.
- [CFNetworkErrors.cfurlErrorCannotParseResponse](cfnetworkerrors/cfurlerrorcannotparseresponse.md)
  The connection can’t parse the server’s response.
- [CFNetworkErrors.cfurlErrorInternationalRoamingOff](cfnetworkerrors/cfurlerrorinternationalroamingoff.md)
  The connection failed because international roaming is disabled on the device.
- [CFNetworkErrors.cfurlErrorCallIsActive](cfnetworkerrors/cfurlerrorcallisactive.md)
  The connection failed because a call is active.
- [CFNetworkErrors.cfurlErrorDataNotAllowed](cfnetworkerrors/cfurlerrordatanotallowed.md)
  The connection failed because data use isn’t currently allowed on the device.
- [CFNetworkErrors.cfurlErrorRequestBodyStreamExhausted](cfnetworkerrors/cfurlerrorrequestbodystreamexhausted.md)
  The connection failed because the request’s body stream was exhausted.
- [CFNetworkErrors.cfurlErrorFileDoesNotExist](cfnetworkerrors/cfurlerrorfiledoesnotexist.md)
  The file operation failed because the file doesn’t exist.
- [CFNetworkErrors.cfurlErrorFileIsDirectory](cfnetworkerrors/cfurlerrorfileisdirectory.md)
  The file operation failed because the file is a directory.
- [CFNetworkErrors.cfurlErrorNoPermissionsToReadFile](cfnetworkerrors/cfurlerrornopermissionstoreadfile.md)
  The file operation failed because it doesn’t have permission to read the file.
- [CFNetworkErrors.cfurlErrorDataLengthExceedsMaximum](cfnetworkerrors/cfurlerrordatalengthexceedsmaximum.md)
  The file operation failed because the file is too large.
- [CFNetworkErrors.cfurlErrorSecureConnectionFailed](cfnetworkerrors/cfurlerrorsecureconnectionfailed.md)
  The secure connection failed for an unknown reason.
- [CFNetworkErrors.cfurlErrorServerCertificateHasBadDate](cfnetworkerrors/cfurlerrorservercertificatehasbaddate.md)
  The secure connection failed because the server’s certificate has an invalid date.
- [CFNetworkErrors.cfurlErrorServerCertificateUntrusted](cfnetworkerrors/cfurlerrorservercertificateuntrusted.md)
  The secure connection failed because the server’s certificate isn’t trusted.
- [CFNetworkErrors.cfurlErrorServerCertificateHasUnknownRoot](cfnetworkerrors/cfurlerrorservercertificatehasunknownroot.md)
  The secure connection failed because the server’s certificate has an unknown root.
- [CFNetworkErrors.cfurlErrorServerCertificateNotYetValid](cfnetworkerrors/cfurlerrorservercertificatenotyetvalid.md)
  The secure connection failed because the server’s certificate isn’t valid yet.
- [CFNetworkErrors.cfurlErrorClientCertificateRejected](cfnetworkerrors/cfurlerrorclientcertificaterejected.md)
  The secure connection failed because the client’s certificate was rejected.
- [CFNetworkErrors.cfurlErrorClientCertificateRequired](cfnetworkerrors/cfurlerrorclientcertificaterequired.md)
  The secure connection failed because the server requires a client certificate.
- [CFNetworkErrors.cfurlErrorCannotLoadFromNetwork](cfnetworkerrors/cfurlerrorcannotloadfromnetwork.md)
  The connection failed because it’s being required to return a cached resource, but one isn’t available.
- [CFNetworkErrors.cfurlErrorCannotCreateFile](cfnetworkerrors/cfurlerrorcannotcreatefile.md)
  The file can’t be created.
- [CFNetworkErrors.cfurlErrorCannotOpenFile](cfnetworkerrors/cfurlerrorcannotopenfile.md)
  The file can’t be opened.
- [CFNetworkErrors.cfurlErrorCannotCloseFile](cfnetworkerrors/cfurlerrorcannotclosefile.md)
  The file can’t be closed.
- [CFNetworkErrors.cfurlErrorCannotWriteToFile](cfnetworkerrors/cfurlerrorcannotwritetofile.md)
  The file can’t be written.
- [CFNetworkErrors.cfurlErrorCannotRemoveFile](cfnetworkerrors/cfurlerrorcannotremovefile.md)
  The file can’t be removed.
- [CFNetworkErrors.cfurlErrorCannotMoveFile](cfnetworkerrors/cfurlerrorcannotmovefile.md)
  The file can’t be moved.
- [CFNetworkErrors.cfurlErrorDownloadDecodingFailedMidStream](cfnetworkerrors/cfurlerrordownloaddecodingfailedmidstream.md)
  The download failed because decoding of the downloaded data failed midstream.
- [CFNetworkErrors.cfurlErrorDownloadDecodingFailedToComplete](cfnetworkerrors/cfurlerrordownloaddecodingfailedtocomplete.md)
  The download failed because decoding of the downloaded data failed to complete.
- [CFNetworkErrors.cfhttpCookieCannotParseCookieFile](cfnetworkerrors/cfhttpcookiecannotparsecookiefile.md)
  The cookie file can’t be parsed.
- [CFNetworkErrors.cfNetServiceErrorUnknown](cfnetworkerrors/cfnetserviceerrorunknown.md)
  An error of unknown type has occurred.
- [CFNetworkErrors.cfNetServiceErrorCollision](cfnetworkerrors/cfnetserviceerrorcollision.md)
  An attempt was made to use a name that’s already in use.
- [CFNetworkErrors.cfNetServiceErrorNotFound](cfnetworkerrors/cfnetserviceerrornotfound.md)
  This error isn’t used.
- [CFNetworkErrors.cfNetServiceErrorInProgress](cfnetworkerrors/cfnetserviceerrorinprogress.md)
  A new search couldn’t be started because a search is already in progress.
- [CFNetworkErrors.cfNetServiceErrorBadArgument](cfnetworkerrors/cfnetserviceerrorbadargument.md)
  A required argument either wasn’t provided or wasn’t valid.
- [CFNetworkErrors.cfNetServiceErrorCancel](cfnetworkerrors/cfnetserviceerrorcancel.md)
  The search or service was canceled.
- [CFNetworkErrors.cfNetServiceErrorInvalid](cfnetworkerrors/cfnetserviceerrorinvalid.md)
  Invalid data was passed to a CFNetServices function.
- [CFNetworkErrors.cfNetServiceErrorTimeout](cfnetworkerrors/cfnetserviceerrortimeout.md)
  Resolution failed because the timeout was reached.
- [CFNetworkErrors.cfNetServiceErrorDNSServiceFailure](cfnetworkerrors/cfnetserviceerrordnsservicefailure.md)
  The DNS service discovery returned an error.
- [CFNetworkErrors.cfurlErrorAppTransportSecurityRequiresSecureConnection](cfnetworkerrors/cfurlerrorapptransportsecurityrequiressecureconnection.md)
  The connection failed because the App Transport Security configuration requires a secure connection.
- [CFNetworkErrors.cfurlErrorBackgroundSessionInUseByAnotherProcess](cfnetworkerrors/cfurlerrorbackgroundsessioninusebyanotherprocess.md)
  The background session failed because it was in use by another process.
- [CFNetworkErrors.cfurlErrorBackgroundSessionWasDisconnected](cfnetworkerrors/cfurlerrorbackgroundsessionwasdisconnected.md)
  The background session failed because it was disconnected.
### Enumeration Cases
- [CFNetworkErrors.cfurlErrorFileOutsideSafeArea](cfnetworkerrors/cfurlerrorfileoutsidesafearea.md)
  The file is outside of the safe area.
### Initializers
- [init?(rawValue: Int32)](cfnetworkerrors/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Error Dictionary Keys](error-dictionary-keys.md)
  Networking-related keys that may be available in a `CFErrorRef` object’s `userInfo` dictionary.
- [Error Domains](error-domains.md)
  High-level error domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors)*