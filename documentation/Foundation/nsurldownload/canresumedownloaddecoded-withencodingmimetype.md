# canResumeDownloadDecoded(withEncodingMIMEType:)

**Framework**: Foundation  
**Kind**: method

Returns whether a URL download object can resume a download that was decoded with the specified MIME type.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class func canResumeDownloadDecoded(withEncodingMIMEType MIMEType: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the URL download object can resume a download that was decoded with the specified MIME type, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The MIME type of a file, in conjunction with the value returned by the [`download(_:shouldDecodeSourceDataOfMIMEType:)`](nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:).md) delegate method, determines whether the `NSURLDownload` class should decode or decompress the incoming data as it is received.

Some compression techniques, such as the `DEFLATE` algorithm (`gzip`) use symbol dictionaries that vary during the compression process, making it impractical to decompress only a portion of the data starting in the middle. For this reason, this method returns [`false`](https://developer.apple.com/documentation/swift/false) unless both of the following conditions are met:

- The MIME type is of a type that the `NSURLDownload` class knows how to decompress or decode.
- The decoding can be safely resumed.

In practice, this method returns [`true`](https://developer.apple.com/documentation/swift/true) for MacBinary and BinHex, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

If your app needs to be able to resume file downloads in `gzip` format, your [`download(_:shouldDecodeSourceDataOfMIMEType:)`](nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:).md) method must return [`false`](https://developer.apple.com/documentation/swift/false), and you must decode the resulting file yourself after you finish downloading it in its entirety.

## Parameters

- `MIMEType`: The MIME type the caller wants to know about.

## See Also

- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](nsurldownload/init(resumedata:delegate:path:).md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var resumeData: Data?](nsurldownload/resumedata.md)
  Returns the resume data for a download that is not yet complete.
- [var deletesFileUponFailure: Bool](nsurldownload/deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/canresumedownloaddecoded(withencodingmimetype:))*