# download(_:didReceive:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didReceive response: URLResponse)
```

```objc
- (void) download:(NSURLDownload *) download didReceiveResponse:(NSURLResponse *) response;
```

## Discussion

In some rare cases, multiple responses may be received for a single download. In this case, the client should assume that each new response resets the download progress to 0 and should check the new response for the expected content length.

## Parameters

- `download`: The URL download object sending the message.
- `response`: The URL response object received as part of the download. `response` is immutable and will not be modified after this method is called.

## See Also

### Download Data and Responses
- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](./download%28_,decidedestinationwithsuggestedfilename%29.md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func downloadDidBegin(NSURLDownload)](./downloaddidbegin%28_%29.md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](./download%28_,didcreatedestination%29.md)
  Sent when the destination file is created.
- [func download(NSURLDownload, didReceiveDataOfLength: Int)](./download%28_,didreceivedataoflength%29.md)
  Sent as a download object receives data incrementally.
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](./download%28_,shoulddecodesourcedataofmimetype%29.md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](./download%28_,willresumewith,frombyte%29.md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](./download%28_,willsend,redirectresponse%29.md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didreceive:)-817z3)*