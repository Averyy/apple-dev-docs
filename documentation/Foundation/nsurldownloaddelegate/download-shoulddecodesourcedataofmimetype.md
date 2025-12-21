# download(_:shouldDecodeSourceDataOfMIMEType:)

**Framework**: Foundation  
**Kind**: method

Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, shouldDecodeSourceDataOfMIMEType encodingType: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to decode the file, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The delegate may receive this message more than once if the file has been encoded multiple times. This method is not called if the downloaded file is not encoded.

## Parameters

- `download`: The URL download object sending the message.
- `encodingType`: The type of encoding used by the downloaded file. The supported encoding formats are MacBinary ( ), Binhex ( ) and gzip ( ).

## See Also

- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:).md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func downloadDidBegin(NSURLDownload)](nsurldownloaddelegate/downloaddidbegin(_:).md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](nsurldownloaddelegate/download(_:didcreatedestination:).md)
  Sent when the destination file is created.
- [func download(NSURLDownload, didReceive: URLResponse)](nsurldownloaddelegate/download(_:didreceive:)-817z3.md)
  Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [func download(NSURLDownload, didReceiveDataOfLength: Int)](nsurldownloaddelegate/download(_:didreceivedataoflength:).md)
  Sent as a download object receives data incrementally.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](nsurldownloaddelegate/download(_:willresumewith:frombyte:).md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](nsurldownloaddelegate/download(_:willsend:redirectresponse:).md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:))*