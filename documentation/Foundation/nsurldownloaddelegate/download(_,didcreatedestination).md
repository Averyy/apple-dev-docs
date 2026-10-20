# download(_:didCreateDestination:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when the destination file is created.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didCreateDestination path: String)
```

```objc
- (void) download:(NSURLDownload *) download didCreateDestination:(NSString *) path;
```

## Parameters

- `download`: The URL download object sending the message.
- `path`: The path to the destination file.

## See Also

### Download Data and Responses
- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](./download%28_,decidedestinationwithsuggestedfilename%29.md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func downloadDidBegin(NSURLDownload)](./downloaddidbegin%28_%29.md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didReceive: URLResponse)](./download%28_,didreceive%29-817z3.md)
  Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [func download(NSURLDownload, didReceiveDataOfLength: Int)](./download%28_,didreceivedataoflength%29.md)
  Sent as a download object receives data incrementally.
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](./download%28_,shoulddecodesourcedataofmimetype%29.md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](./download%28_,willresumewith,frombyte%29.md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](./download%28_,willsend,redirectresponse%29.md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didcreatedestination:))*