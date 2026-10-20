# deletesFileUponFailure

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

**Availability**:
- macOS 10.2+

## Declaration

```swift
var deletesFileUponFailure: Bool { get set }
```

```objc
@property BOOL deletesFileUponFailure;
```

#### Return Value

[`true`](../../Swift/true.md) if partially downloaded files should be deleted when a download stops prematurely, [`false`](../../Swift/false.md) otherwise. The default is [`true`](../../Swift/true.md).

## See Also

### Resuming partial downloads
- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](./canresumedownloaddecoded%28withencodingmimetype%29.md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](./init%28resumedata,delegate,path%29.md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var resumeData: Data?](./resumedata.md)
  Returns the resume data for a download that is not yet complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/deletesfileuponfailure)*