# download(_:decideDestinationWithSuggestedFilename:)

**Framework**: Foundation  
**Kind**: method

The delegate receives this message when `download` has determined a suggested filename for the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, decideDestinationWithSuggestedFilename filename: String)
```

#### Discussion

The suggested filename is either derived from the last path component of the URL and the MIME type or, if the download was encoded, from the encoding. If the delegate wishes to modify the path, it should send [`setDestination(_:allowOverwrite:)`](nsurldownload/setdestination(_:allowoverwrite:).md) to `download`.

##### Special Considerations

The delegate will not receive this message if `setDestination:allowOverwrite:` has already been called for the download.

## Parameters

- `download`: The URL download object sending the message.
- `filename`: The suggested filename for the download.

## See Also

- [func downloadDidBegin(NSURLDownload)](nsurldownloaddelegate/downloaddidbegin(_:).md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](nsurldownloaddelegate/download(_:didcreatedestination:).md)
  Sent when the destination file is created.
- [func download(NSURLDownload, didReceive: URLResponse)](nsurldownloaddelegate/download(_:didreceive:)-817z3.md)
  Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [func download(NSURLDownload, didReceiveDataOfLength: Int)](nsurldownloaddelegate/download(_:didreceivedataoflength:).md)
  Sent as a download object receives data incrementally.
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:).md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](nsurldownloaddelegate/download(_:willresumewith:frombyte:).md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](nsurldownloaddelegate/download(_:willsend:redirectresponse:).md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:))*