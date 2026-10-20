# download(_:willSend:redirectResponse:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when the download object determines that it must change URLs in order to continue loading a request.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, willSend request: URLRequest, redirectResponse: URLResponse?) -> URLRequest?
```

```objc
- (NSURLRequest *) download:(NSURLDownload *) download willSendRequest:(NSURLRequest *) request redirectResponse:(NSURLResponse *) redirectResponse;
```

#### Return Value

The actual URL request to use in light of the redirection response. The delegate may copy and modify `request` as necessary to change its attributes, return `request` unmodified, or return `nil`.

#### Discussion

If the delegate wishes to cancel the redirect, it should call the `download` object’s [`cancel()`](../nsurldownload/cancel%28%29.md) method. Alternatively, the delegate method can return `nil` to cancel the redirect, and the download will continue to process. This has special relevance in the case where `redirectResponse` is not `nil`. In this case, any data that is loaded for the download will be sent to the delegate, and the delegate will receive a [`downloadDidFinish(_:)`](./downloaddidfinish%28_%29.md) or [`download(_:didFailWithError:)`](./download%28_,didfailwitherror%29.md) message, as appropriate.

##### Special Considerations

The delegate can receive this message as a result of transforming a request’s URL to its canonical form, or for protocol-specific reasons, such as an HTTP redirect. The delegate implementation should be prepared to receive this message multiple times.

## Parameters

- `download`: The URL download object sending the message.
- `request`: The proposed redirected request. The delegate should inspect the redirected request to verify that it meets its needs, and create a copy with new attributes to return to the connection if necessary.
- `redirectResponse`: The URL response that caused the redirect. May be `nil` in cases where this method is not being sent as a result of involving the delegate in redirect processing.

## See Also

### Download Data and Responses
- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](./download%28_,decidedestinationwithsuggestedfilename%29.md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:willsend:redirectresponse:))*