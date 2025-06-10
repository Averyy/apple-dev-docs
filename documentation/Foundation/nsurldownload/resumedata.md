# resumeData

**Framework**: Foundation  
**Kind**: property

Returns the resume data for a download that is not yet complete.

**Availability**:
- macOS 10.2+

## Declaration

```swift
var resumeData: Data? { get }
```

#### Return Value

The resume data for a download that is not yet complete. This data represents the necessary state information that an `NSURLDownload` object needs to resume a download. The resume data can later be used when initializing a download with [`init(resumeData:delegate:path:)`](nsurldownload/init(resumedata:delegate:path:).md). Returns `nil` if the download is not able to be resumed.

#### Discussion

Resume data is returned only if both the protocol and the server support resuming. For details on how to resume a connection, see the documentation for [`init(resumeData:delegate:path:)`](nsurldownload/init(resumedata:delegate:path:).md).

## See Also

- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](nsurldownload/canresumedownloaddecoded(withencodingmimetype:).md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](nsurldownload/init(resumedata:delegate:path:).md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var deletesFileUponFailure: Bool](nsurldownload/deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/resumedata)*