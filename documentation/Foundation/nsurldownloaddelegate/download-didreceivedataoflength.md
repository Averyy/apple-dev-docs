# download(_:didReceiveDataOfLength:)

**Framework**: Foundation  
**Kind**: method

Sent as a download object receives data incrementally.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didReceiveDataOfLength length: Int)
```

## Parameters

- `download`: The URL download object sending the message.
- `length`: The amount of data received in this increment of the download, measured in bytes.

## See Also

- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:).md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func downloadDidBegin(NSURLDownload)](nsurldownloaddelegate/downloaddidbegin(_:).md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](nsurldownloaddelegate/download(_:didcreatedestination:).md)
  Sent when the destination file is created.
- [func download(NSURLDownload, didReceive: URLResponse)](nsurldownloaddelegate/download(_:didreceive:)-817z3.md)
  Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:).md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](nsurldownloaddelegate/download(_:willresumewith:frombyte:).md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](nsurldownloaddelegate/download(_:willsend:redirectresponse:).md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didreceivedataoflength:))*