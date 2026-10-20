# download(_:decideDestinationWithSuggestedFilename:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

The delegate receives this message when `download` has determined a suggested filename for the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, decideDestinationWithSuggestedFilename filename: String)
```

```objc
- (void) download:(NSURLDownload *) download decideDestinationWithSuggestedFilename:(NSString *) filename;
```

#### Discussion

The suggested filename is either derived from the last path component of the URL and the MIME type or, if the download was encoded, from the encoding. If the delegate wishes to modify the path, it should send [`setDestination(_:allowOverwrite:)`](../nsurldownload/setdestination%28_,allowoverwrite%29.md) to `download`.

##### Special Considerations

The delegate will not receive this message if `setDestination:allowOverwrite:` has already been called for the download.

## Parameters

- `download`: The URL download object sending the message.
- `filename`: The suggested filename for the download.

## See Also

### Download Data and Responses
- [func downloadDidBegin(NSURLDownload)](./downloaddidbegin%28_%29.md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](./download%28_,didcreatedestination%29.md)
  Sent when the destination file is created.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:))*