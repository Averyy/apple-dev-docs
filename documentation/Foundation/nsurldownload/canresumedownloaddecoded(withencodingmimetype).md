# canResumeDownloadDecoded(withEncodingMIMEType:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns whether a URL download object can resume a download that was decoded with the specified MIME type.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class func canResumeDownloadDecoded(withEncodingMIMEType MIMEType: String) -> Bool
```

```objc
+ (BOOL) canResumeDownloadDecodedWithEncodingMIMEType:(NSString *) MIMEType;
```

## Return Value

[`true`](../../Swift/true.md) if the URL download object can resume a download that was decoded with the specified MIME type, [`false`](../../Swift/false.md) otherwise.

## Discussion

The MIME type of a file, in conjunction with the value returned by the [`download(_:shouldDecodeSourceDataOfMIMEType:)`](../nsurldownloaddelegate/download%28_,shoulddecodesourcedataofmimetype%29.md) delegate method, determines whether the `NSURLDownload` class should decode or decompress the incoming data as it is received.

Some compression techniques, such as the `DEFLATE` algorithm (`gzip`) use symbol dictionaries that vary during the compression process, making it impractical to decompress only a portion of the data starting in the middle. For this reason, this method returns [`false`](../../Swift/false.md) unless both of the following conditions are met:

- The MIME type is of a type that the `NSURLDownload` class knows how to decompress or decode.
- The decoding can be safely resumed.

In practice, this method returns [`true`](../../Swift/true.md) for MacBinary and BinHex, otherwise [`false`](../../Swift/false.md).

If your app needs to be able to resume file downloads in `gzip` format, your [`download(_:shouldDecodeSourceDataOfMIMEType:)`](../nsurldownloaddelegate/download%28_,shoulddecodesourcedataofmimetype%29.md) method must return [`false`](../../Swift/false.md), and you must decode the resulting file yourself after you finish downloading it in its entirety.

## Parameters

- `MIMEType`: The MIME type the caller wants to know about.

## See Also

### Resuming partial downloads
- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](./init%28resumedata,delegate,path%29.md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var resumeData: Data?](./resumedata.md)
  Returns the resume data for a download that is not yet complete.
- [var deletesFileUponFailure: Bool](./deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/canresumedownloaddecoded(withencodingmimetype:))*