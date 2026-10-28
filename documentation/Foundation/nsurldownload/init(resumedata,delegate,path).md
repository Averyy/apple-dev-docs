# init(resumeData:delegate:path:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.

**Availability**:
- macOS 10.3+ - Deprecated in 10.11

> **Deprecated**: Use NSURLSession downloadTask (see NSURLSession.h)

## Declaration

```swift
init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)
```

```objc
- (instancetype) initWithResumeData:(NSData *) resumeData delegate:(id<NSURLDownloadDelegate>) delegate path:(NSString *) path;
```

## Return Value

An initialized NSURLDownload object.

## Discussion

If you want to support pausing and resuming downloads, your app must:

1. Call [`deletesFileUponFailure`](./deletesfileuponfailure.md), passing [`false`](../../Swift/false.md). If you want to support resuming downloads in the event of a lost connection, you should do this immediately after you initialize the download object.
2. If your app needs to pause the transfer for any reason, call [`cancel()`](./cancel%28%29.md). Because your app previously called [`deletesFileUponFailure`](./deletesfileuponfailure.md) with [`false`](../../Swift/false.md), the in-progress download is not deleted.
3. After your app pauses the transfer or after a transfer error occurs, call [`resumeData`](./resumedata.md) to obtain the data needed to resume the transfer later.

> **Note**:  Resume data is returned only if both the protocol and the server support resuming.
>
> In addition, a download of compressed content cannot be resumed if `NSURLDownload` is configured to decompress that data on the fly; for details, read the documentation for the [`canResumeDownloadDecoded(withEncodingMIMEType:)`](./canresumedownloaddecoded%28withencodingmimetype%29.md) method.

1. If the transfer failed because of a connectivity error, use the `SCNetworkReachability` API to determine an appropriate time to try again. For details, read [`SCNetworkReachability`](../../SystemConfiguration/scnetworkreachability.md).

If your app explicitly paused the download, wait until it is appropriate to continue the transfer (such as when the user clicks or taps a resume button). 5. Call [`init(resumeData:delegate:path:)`](./init%28resumedata,delegate,path%29.md) and pass the resume data blob that it previously obtained in step 3.

## Parameters

- `resumeData`: Specifies the data to resume downloading.
- `delegate`: The delegate for the download. This object will receive delegate messages as the download progresses. Delegate messages will be sent on the thread which calls this method. For the download to work correctly the calling thread’s run loop must be operating in the default run loop mode.

  The `NSURLDownload` class maintains a strong reference to this delegate object.
- `path`: The location for the downloaded data.

## See Also

### Related Documentation
- [func cancel()](./cancel%28%29.md)
  Cancels the receiver’s download and deletes the downloaded file.
### Resuming partial downloads
- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](./canresumedownloaddecoded%28withencodingmimetype%29.md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [var resumeData: Data?](./resumedata.md)
  Returns the resume data for a download that is not yet complete.
- [var deletesFileUponFailure: Bool](./deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/init(resumedata:delegate:path:))*