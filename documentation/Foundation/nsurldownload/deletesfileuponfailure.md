# deletesFileUponFailure

**Framework**: Foundation  
**Kind**: property

Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

**Availability**:
- macOS 10.2+

## Declaration

```swift
var deletesFileUponFailure: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if partially downloaded files should be deleted when a download stops prematurely, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. The default is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](nsurldownload/canresumedownloaddecoded(withencodingmimetype:).md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](nsurldownload/init(resumedata:delegate:path:).md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var resumeData: Data?](nsurldownload/resumedata.md)
  Returns the resume data for a download that is not yet complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/deletesfileuponfailure)*