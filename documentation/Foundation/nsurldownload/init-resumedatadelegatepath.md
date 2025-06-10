# init(resumeData:delegate:path:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.

**Availability**:
- macOS 10.3+

## Declaration

```swift
init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)
```

#### Return Value

An initialized NSURLDownload object.

#### Discussion

If you want to support pausing and resuming downloads, your app must:

1. Call [`deletesFileUponFailure`](nsurldownload/deletesfileuponfailure.md), passing [`false`](https://developer.apple.com/documentation/swift/false). If you want to support resuming downloads in the event of a lost connection, you should do this immediately after you initialize the download object.
2. If your app needs to pause the transfer for any reason, call [`cancel()`](nsurldownload/cancel().md). Because your app previously called [`deletesFileUponFailure`](nsurldownload/deletesfileuponfailure.md) with [`false`](https://developer.apple.com/documentation/swift/false), the in-progress download is not deleted.
3. After your app pauses the transfer or after a transfer error occurs, call [`resumeData`](nsurldownload/resumedata.md) to obtain the data needed to resume the transfer later.

> **Note**:  Resume data is returned only if both the protocol and the server support resuming. In addition, a download of compressed content cannot be resumed if `NSURLDownload` is configured to decompress that data on the fly; for details, read the documentation for the [`canResumeDownloadDecoded(withEncodingMIMEType:)`](nsurldownload/canresumedownloaddecoded(withencodingmimetype:).md) method.

1. If the transfer failed because of a connectivity error, use the `SCNetworkReachability` API to determine an appropriate time to try again. For details, read [`SCNetworkReachability`](https://developer.apple.com/documentation/SystemConfiguration/SCNetworkReachability).

If your app explicitly paused the download, wait until it is appropriate to continue the transfer (such as when the user clicks or taps a resume button). 5. Call [`init(resumeData:delegate:path:)`](nsurldownload/init(resumedata:delegate:path:).md) and pass the resume data blob that it previously obtained in step 3.

## Parameters

- `resumeData`: Specifies the data to resume downloading.
- `delegate`: The   class maintains a strong reference to this delegate object.
- `path`: The location for the downloaded data.

## See Also

- [func cancel()](nsurldownload/cancel.md)
  Cancels the receiver’s download and deletes the downloaded file.
- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](nsurldownload/canresumedownloaddecoded(withencodingmimetype:).md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [var resumeData: Data?](nsurldownload/resumedata.md)
  Returns the resume data for a download that is not yet complete.
- [var deletesFileUponFailure: Bool](nsurldownload/deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/init(resumedata:delegate:path:))*