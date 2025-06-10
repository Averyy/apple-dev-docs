# download(_:willSend:redirectResponse:)

**Framework**: Foundation  
**Kind**: method

Sent when the download object determines that it must change URLs in order to continue loading a request.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, willSend request: URLRequest, redirectResponse: URLResponse?) -> URLRequest?
```

#### Return Value

The actual URL request to use in light of the redirection response. The delegate may copy and modify `request` as necessary to change its attributes, return `request` unmodified, or return `nil`.

#### Discussion

If the delegate wishes to cancel the redirect, it should call the `download` object’s [`cancel()`](nsurldownload/cancel().md) method. Alternatively, the delegate method can return `nil` to cancel the redirect, and the download will continue to process. This has special relevance in the case where `redirectResponse` is not `nil`. In this case, any data that is loaded for the download will be sent to the delegate, and the delegate will receive a [`downloadDidFinish(_:)`](nsurldownloaddelegate/downloaddidfinish(_:).md) or [`download(_:didFailWithError:)`](nsurldownloaddelegate/download(_:didfailwitherror:).md) message, as appropriate.

##### Special Considerations

The delegate can receive this message as a result of transforming a request’s URL to its canonical form, or for protocol-specific reasons, such as an HTTP redirect. The delegate implementation should be prepared to receive this message multiple times.

## Parameters

- `download`: The URL download object sending the message.
- `request`: The proposed redirected request. The delegate should inspect the redirected request to verify that it meets its needs, and create a copy with new attributes to return to the connection if necessary.
- `redirectResponse`: The URL response that caused the redirect. May be   in cases where this method is not being sent as a result of involving the delegate in redirect processing.

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
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](nsurldownloaddelegate/download(_:shoulddecodesourcedataofmimetype:).md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](nsurldownloaddelegate/download(_:willresumewith:frombyte:).md)
  Sent when a download object has received a response from the server after attempting to resume a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:willsend:redirectresponse:))*