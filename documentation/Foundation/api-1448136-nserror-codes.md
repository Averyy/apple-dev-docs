# NSError Codes

**Framework**: Foundation

Error codes in the Cocoa error domain.

#### Overview

The constants in this enumeration are [`NSError`](nserror.md) code numbers in the Cocoa error domain ([`NSCocoaErrorDomain`](nscocoaerrordomain.md)). Other frameworks, most notably the Application Kit, provide their own [`NSCocoaErrorDomain`](nscocoaerrordomain.md) error codes.

The enumeration constants beginning with `NSFile` indicate file-system errors or errors related to file I/O operations. Use the key [`NSFilePathErrorKey`](nsfilepatherrorkey.md) or the [`NSURLErrorKey`](nsurlerrorkey.md) (whichever is appropriate) to access the file-system path or URL in the [`userInfo`](nserror/userinfo.md) dictionary of the [`NSError`](nserror.md) object.

## Topics

### Bundle Errors
- [var NSBundleErrorMinimum: Int](nsbundleerrorminimum-swift.var.md)
  The start of the range of error codes reserved for bundle errors.
- [var NSBundleErrorMaximum: Int](nsbundleerrormaximum-swift.var.md)
  The end of the range of error codes reserved for bundle errors.
- [var NSBundleOnDemandResourceExceededMaximumSizeError: Int](nsbundleondemandresourceexceededmaximumsizeerror-swift.var.md)
  The application exceeded the amount of on-demand resources content in use at one time.
- [var NSBundleOnDemandResourceInvalidTagError: Int](nsbundleondemandresourceinvalidtagerror-swift.var.md)
  The application specified a tag that the system couldn’t find in the application tag manifest.
- [var NSBundleOnDemandResourceOutOfSpaceError: Int](nsbundleondemandresourceoutofspaceerror-swift.var.md)
  Insufficient space available to download the requested on-demand resources.
### Cancellation
- [var NSUserCancelledError: Int](nsusercancellederror-swift.var.md)
  The user canceled the operation (for example, by pressing Command-period).
### Cloud-Sharing Errors
- [var NSCloudSharingErrorMinimum: Int](nscloudsharingerrorminimum-swift.var.md)
  The start of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingErrorMaximum: Int](nscloudsharingerrormaximum-swift.var.md)
  The end of the range of error codes reserved for cloud-sharing errors.
- [var NSCloudSharingConflictError: Int](nscloudsharingconflicterror-swift.var.md)
  A conflict occurred during an attempt to save changes.
- [var NSCloudSharingNetworkFailureError: Int](nscloudsharingnetworkfailureerror-swift.var.md)
  Sharing failed due to a network failure.
- [var NSCloudSharingNoPermissionError: Int](nscloudsharingnopermissionerror-swift.var.md)
  The current user doesn’t have permission to perform the requested actions.
- [var NSCloudSharingOtherError: Int](nscloudsharingothererror-swift.var.md)
  An otherwise unspecified cloud-sharing error occurred.
- [var NSCloudSharingQuotaExceededError: Int](nscloudsharingquotaexceedederror-swift.var.md)
  The user doesn’t have enough storage space available to share the requested items.
- [var NSCloudSharingTooManyParticipantsError: Int](nscloudsharingtoomanyparticipantserror-swift.var.md)
  Additional participants couldn’t be added to the share, because the limit was reached.
### Coder Errors
- [var NSCoderErrorMinimum: Int](nscodererrorminimum-swift.var.md)
  The start of the range of error codes reserved for coder errors.
- [var NSCoderErrorMaximum: Int](nscodererrormaximum-swift.var.md)
  The end of the range of error codes reserved for coder errors.
- [var NSCoderValueNotFoundError: Int](nscodervaluenotfounderror-swift.var.md)
  The requested data wasn’t found.
- [var NSCoderReadCorruptError: Int](nscoderreadcorrupterror-swift.var.md)
  Decoding failed due to corrupt data.
### Executable Errors
- [var NSExecutableErrorMinimum: Int](nsexecutableerrorminimum-swift.var.md)
  The beginning of the range of error codes reserved for errors related to executable files.
- [var NSExecutableErrorMaximum: Int](nsexecutableerrormaximum-swift.var.md)
  The end of the range of error codes reserved for errors related to executable files.
- [var NSExecutableArchitectureMismatchError: Int](nsexecutablearchitecturemismatcherror-swift.var.md)
  The executable doesn’t provide an architecture compatible with the current process.
- [var NSExecutableLinkError: Int](nsexecutablelinkerror-swift.var.md)
  The executable failed due to linking issues.
- [var NSExecutableLoadError: Int](nsexecutableloaderror-swift.var.md)
  Executable cannot be loaded for an otherwise-unspecified reason.
- [var NSExecutableNotLoadableError: Int](nsexecutablenotloadableerror-swift.var.md)
  The executable type isn’t loadable in the current process.
- [var NSExecutableRuntimeMismatchError: Int](nsexecutableruntimemismatcherror-swift.var.md)
  The executable has Objective-C runtime information that’s incompatible with the current process.
### Formatting Errors
- [var NSFormattingErrorMinimum: Int](nsformattingerrorminimum-swift.var.md)
  The start of the range of error codes reserved for formatting errors.
- [var NSFormattingErrorMaximum: Int](nsformattingerrormaximum-swift.var.md)
  The end of the range of error codes reserved for formatting errors.
- [var NSFormattingError: Int](nsformattingerror-swift.var.md)
  A formatter couldn’t generate a string for an object, or parse a string into an object.
### File Errors
- [var NSFileErrorMinimum: Int](nsfileerrorminimum-swift.var.md)
  The start of the range of error codes reserved for file errors.
- [var NSFileErrorMaximum: Int](nsfileerrormaximum-swift.var.md)
  The end of the range of error codes reserved for file errors.
- [var NSFileLockingError: Int](nsfilelockingerror-swift.var.md)
  The file could not be locked.
- [var NSFileManagerUnmountBusyError: Int](nsfilemanagerunmountbusyerror-swift.var.md)
  The volume couldn’t be unmounted because it’s in use.
- [var NSFileManagerUnmountUnknownError: Int](nsfilemanagerunmountunknownerror-swift.var.md)
  The volume couldn’t be unmounted, for unknown reasons.
- [var NSFileNoSuchFileError: Int](nsfilenosuchfileerror-swift.var.md)
  A filesystem operation was attempted on a non-existent file.
### File Reading Errors
- [var NSFileReadCorruptFileError: Int](nsfilereadcorruptfileerror-swift.var.md)
  Could not read because of a corrupted file, bad format, or similar reason.
- [var NSFileReadInapplicableStringEncodingError: Int](nsfilereadinapplicablestringencodingerror-swift.var.md)
  Could not read because the string encoding wasn’t applicable.
- [var NSFileReadInvalidFileNameError: Int](nsfilereadinvalidfilenameerror-swift.var.md)
  Could not read because of an invalid file name.
- [var NSFileReadNoPermissionError: Int](nsfilereadnopermissionerror-swift.var.md)
  Could not read because of a permission problem.
- [var NSFileReadNoSuchFileError: Int](nsfilereadnosuchfileerror-swift.var.md)
  Could not read because no such file was found.
- [var NSFileReadTooLargeError: Int](nsfilereadtoolargeerror-swift.var.md)
  Could not read because the specified file was too large.
- [var NSFileReadUnknownError: Int](nsfilereadunknownerror-swift.var.md)
  Could not read, for unknown reasons.
- [var NSFileReadUnknownStringEncodingError: Int](nsfilereadunknownstringencodingerror-swift.var.md)
  Could not read because the string coding of the file couldn’t be determined.
- [var NSFileReadUnsupportedSchemeError: Int](nsfilereadunsupportedschemeerror-swift.var.md)
  Could not read because the specified URL scheme is unsupported.
### File Writing Errors
- [var NSFileWriteFileExistsError: Int](nsfilewritefileexistserror-swift.var.md)
  Could not perform an operation because the destination file already exists.
- [var NSFileWriteInapplicableStringEncodingError: Int](nsfilewriteinapplicablestringencodingerror-swift.var.md)
  Could not write because the string encoding was not applicable.
- [var NSFileWriteInvalidFileNameError: Int](nsfilewriteinvalidfilenameerror-swift.var.md)
  Could not write because of an invalid file name.
- [var NSFileWriteNoPermissionError: Int](nsfilewritenopermissionerror-swift.var.md)
  Could not write because of a permission problem.
- [var NSFileWriteOutOfSpaceError: Int](nsfilewriteoutofspaceerror-swift.var.md)
  Could not write because of a lack of disk space.
- [var NSFileWriteUnknownError: Int](nsfilewriteunknownerror-swift.var.md)
  Could not write, for unknown reasons.
- [var NSFileWriteUnsupportedSchemeError: Int](nsfilewriteunsupportedschemeerror-swift.var.md)
  Could not write because the specified URL scheme is unsupported.
- [var NSFileWriteVolumeReadOnlyError: Int](nsfilewritevolumereadonlyerror-swift.var.md)
  Could not write because the volume is read-only.
### iCloud File Errors
- [var NSUbiquitousFileErrorMinimum: Int](nsubiquitousfileerrorminimum-swift.var.md)
  The minimum error code value that represents an iCloud error.
- [var NSUbiquitousFileErrorMaximum: Int](nsubiquitousfileerrormaximum-swift.var.md)
  The maximum error code value that represents an iCloud error.
- [var NSUbiquitousFileNotUploadedDueToQuotaError: Int](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md)
  The item could not be uploaded to iCloud because it would make the account go over its quota.
- [var NSUbiquitousFileUbiquityServerNotAvailable: Int](nsubiquitousfileubiquityservernotavailable-swift.var.md)
  A failure to connect to the iCloud servers.
- [var NSUbiquitousFileUnavailableError: Int](nsubiquitousfileunavailableerror-swift.var.md)
  The item has not been uploaded to iCloud by another device yet.
### Property List Errors
- [var NSPropertyListErrorMinimum: Int](nspropertylisterrorminimum-swift.var.md)
  The start of the range of error codes reserved for property list errors.
- [var NSPropertyListErrorMaximum: Int](nspropertylisterrormaximum-swift.var.md)
  The end of the range of error codes reserved for property list errors.
- [var NSPropertyListReadCorruptError: Int](nspropertylistreadcorrupterror-swift.var.md)
  Parsing of the property list failed.
- [var NSPropertyListReadStreamError: Int](nspropertylistreadstreamerror-swift.var.md)
  Reading of the property list failed.
- [var NSPropertyListReadUnknownVersionError: Int](nspropertylistreadunknownversionerror-swift.var.md)
  The version number of the property list cannot be determined.
- [var NSPropertyListWriteInvalidError: Int](nspropertylistwriteinvaliderror-swift.var.md)
  Writing failed because of an invalid property list object, or an invalid property list type was specified.
- [var NSPropertyListWriteStreamError: Int](nspropertylistwritestreamerror-swift.var.md)
  Writing to the property list failed.
### User Activity Errors
- [var NSUserActivityErrorMinimum: Int](nsuseractivityerrorminimum-swift.var.md)
  The start of the range of error codes reserved for user activity errors.
- [var NSUserActivityErrorMaximum: Int](nsuseractivityerrormaximum-swift.var.md)
  The end of the range of error codes reserved for user activity errors.
- [var NSUserActivityConnectionUnavailableError: Int](nsuseractivityconnectionunavailableerror-swift.var.md)
  The user activity couldn’t be continued because a required connection wasn’t available.
- [var NSUserActivityHandoffFailedError: Int](nsuseractivityhandofffailederror-swift.var.md)
  The data for the user activity wasn’t available.
- [var NSUserActivityHandoffUserInfoTooLargeError: Int](nsuseractivityhandoffuserinfotoolargeerror-swift.var.md)
  The user info dictionary was too large to receive.
- [var NSUserActivityRemoteApplicationTimedOutError: Int](nsuseractivityremoteapplicationtimedouterror-swift.var.md)
  The remote application failed to send data within the specified time.
### Validation Errors
- [var NSValidationErrorMinimum: Int](nsvalidationerrorminimum-swift.var.md)
  The start of the range of error codes reserved for validation errors.
- [var NSValidationErrorMaximum: Int](nsvalidationerrormaximum-swift.var.md)
  The end of the range of error codes reserved for validation errors.
### XPC Errors
- [var NSXPCConnectionErrorMinimum: Int](nsxpcconnectionerrorminimum-swift.var.md)
  The lower bounds of XPC connection error code values.
- [var NSXPCConnectionErrorMaximum: Int](nsxpcconnectionerrormaximum-swift.var.md)
  The upper bounds of XPC connection error code values.
- [var NSXPCConnectionInterrupted: Int](nsxpcconnectioninterrupted-swift.var.md)
  The XPC connection was interrupted.
- [var NSXPCConnectionInvalid: Int](nsxpcconnectioninvalid-swift.var.md)
  The XPC connection was invalid.
- [var NSXPCConnectionReplyInvalid: Int](nsxpcconnectionreplyinvalid-swift.var.md)
  The XPC connection reply was invalid.
### URL Errors
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
- [var NSURLErrorCannotMoveFile: Int](nsurlerrorcannotmovefile-swift.var.md)
  A downloaded file on disk couldn’t be moved.
- [var NSURLErrorCannotOpenFile: Int](nsurlerrorcannotopenfile-swift.var.md)
  A downloaded file on disk couldn’t be opened.
- [var NSURLErrorCannotParseResponse: Int](nsurlerrorcannotparseresponse-swift.var.md)
  A response to a connection request couldn’t be parsed.
- [var NSURLErrorCannotRemoveFile: Int](nsurlerrorcannotremovefile-swift.var.md)
  A downloaded file couldn’t be removed from disk.
- [var NSURLErrorCannotWriteToFile: Int](nsurlerrorcannotwritetofile-swift.var.md)
  A download task couldn’t write the file to disk.
- [var NSURLErrorClientCertificateRejected: Int](nsurlerrorclientcertificaterejected-swift.var.md)
  A server certificate was rejected.
- [var NSURLErrorClientCertificateRequired: Int](nsurlerrorclientcertificaterequired-swift.var.md)
  A client certificate was required to authenticate an SSL connection during a connection request.
- [var NSURLErrorDNSLookupFailed: Int](nsurlerrordnslookupfailed-swift.var.md)
  The host address couldn’t be found via DNS lookup.
- [var NSURLErrorDataLengthExceedsMaximum: Int](nsurlerrordatalengthexceedsmaximum-swift.var.md)
  The length of the resource data exceeded the maximum allowed.
- [var NSURLErrorDataNotAllowed: Int](nsurlerrordatanotallowed-swift.var.md)
  The cellular network disallowed a connection.
- [var NSURLErrorDownloadDecodingFailedMidStream: Int](nsurlerrordownloaddecodingfailedmidstream-swift.var.md)
  A download task failed to decode an encoded file during the download.
- [var NSURLErrorDownloadDecodingFailedToComplete: Int](nsurlerrordownloaddecodingfailedtocomplete-swift.var.md)
  A download task failed to decode an encoded file after downloading.
- [var NSURLErrorFileDoesNotExist: Int](nsurlerrorfiledoesnotexist-swift.var.md)
  The specified file doesn’t exist.
- [var NSURLErrorFileIsDirectory: Int](nsurlerrorfileisdirectory-swift.var.md)
  A request for an FTP file resulted in the server responding that the file is not a plain file, but a directory.
- [var NSURLErrorFileOutsideSafeArea: Int](nsurlerrorfileoutsidesafearea-swift.var.md)
  An internal file operation failed.
- [var NSURLErrorHTTPTooManyRedirects: Int](nsurlerrorhttptoomanyredirects-swift.var.md)
  A redirect loop was detected or the threshold for number of allowable redirects was exceeded (currently 16).
- [var NSURLErrorInternationalRoamingOff: Int](nsurlerrorinternationalroamingoff-swift.var.md)
  The attempted connection required activating a data context while roaming, but international roaming is disabled.
- [var NSURLErrorNetworkConnectionLost: Int](nsurlerrornetworkconnectionlost-swift.var.md)
  A client or server connection was severed in the middle of an in-progress load.
- [var NSURLErrorNoPermissionsToReadFile: Int](nsurlerrornopermissionstoreadfile-swift.var.md)
  A resource couldn’t be read because of insufficient permissions.
- [var NSURLErrorNotConnectedToInternet: Int](nsurlerrornotconnectedtointernet-swift.var.md)
  A network resource was requested, but an internet connection has not been established and can’t be established automatically.
- [var NSURLErrorRedirectToNonExistentLocation: Int](nsurlerrorredirecttononexistentlocation-swift.var.md)
  A redirect was specified by way of server response code, but the server didn’t accompany this code with a redirect URL.
- [var NSURLErrorRequestBodyStreamExhausted: Int](nsurlerrorrequestbodystreamexhausted-swift.var.md)
  A body stream was needed but the client did not provide one.
- [var NSURLErrorResourceUnavailable: Int](nsurlerrorresourceunavailable-swift.var.md)
  A requested resource couldn’t be retrieved.
- [var NSURLErrorSecureConnectionFailed: Int](nsurlerrorsecureconnectionfailed-swift.var.md)
  An attempt to establish a secure connection failed for reasons that can’t be expressed more specifically.
- [var NSURLErrorServerCertificateHasBadDate: Int](nsurlerrorservercertificatehasbaddate-swift.var.md)
  A server certificate is expired, or is not yet valid.
- [var NSURLErrorServerCertificateHasUnknownRoot: Int](nsurlerrorservercertificatehasunknownroot-swift.var.md)
  A server certificate wasn’t signed by any root server.
- [var NSURLErrorServerCertificateNotYetValid: Int](nsurlerrorservercertificatenotyetvalid-swift.var.md)
  A server certificate isn’t valid yet.
- [var NSURLErrorServerCertificateUntrusted: Int](nsurlerrorservercertificateuntrusted-swift.var.md)
  A server certificate was signed by a root server that isn’t trusted.
- [var NSURLErrorTimedOut: Int](nsurlerrortimedout-swift.var.md)
  An asynchronous operation timed out.
- [var NSURLErrorUnknown: Int](nsurlerrorunknown-swift.var.md)
  The URL Loading System encountered an error that it can’t interpret.
- [var NSURLErrorUnsupportedURL: Int](nsurlerrorunsupportedurl-swift.var.md)
  A properly formed URL couldn’t be handled by the framework.
- [var NSURLErrorUserAuthenticationRequired: Int](nsurlerroruserauthenticationrequired-swift.var.md)
  Authentication was required to access a resource.
- [var NSURLErrorUserCancelledAuthentication: Int](nsurlerrorusercancelledauthentication-swift.var.md)
  An asynchronous request for authentication has been canceled by the user.
- [var NSURLErrorZeroByteResource: Int](nsurlerrorzerobyteresource-swift.var.md)
  A server reported that a URL has a non-zero content length, but terminated the network connection gracefully without sending any data.
### Miscellaneous Errors
- [var NSFeatureUnsupportedError: Int](nsfeatureunsupportederror-swift.var.md)
  The feature isn’t supported, because the file system lacks the feature, or required libraries are missing, or other similar reasons.
- [var NSKeyValueValidationError: Int](nskeyvaluevalidationerror-swift.var.md)
  A key-value coding validation error.

## See Also

- [struct CocoaError](cocoaerror.md)
  Describes errors within the Cocoa error domain.
- [struct MachError](macherror.md)
  Describes an error in the Mach error domain.
- [struct POSIXError](posixerror.md)
  Describes an error in the POSIX error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1448136-nserror-codes)*