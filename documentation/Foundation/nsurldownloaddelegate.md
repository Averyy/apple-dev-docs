# NSURLDownloadDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

A protocol that URL download delegates implement to interact with a URL download request.

**Availability**:
- macOS 10.2+

## Declaration

```swift
protocol NSURLDownloadDelegate : NSObjectProtocol
```

```objc
@protocol NSURLDownloadDelegate <NSObject>
```

#### Overview

The [`NSURLDownloadDelegate`](./nsurldownloaddelegate.md) protocol defines methods that allow an object to receive informational callbacks about the asynchronous load of a download’s URL request. Other delegate methods provide facilities that allow the delegate to customize the process of performing an asynchronous URL load.

Note that these delegate methods will be called on the thread that started the asynchronous load operation for the associated [`NSURLDownload`](./nsurldownload.md) object.

- A [`downloadDidBegin(_:)`](./nsurldownloaddelegate/downloaddidbegin%28_%29.md) message will be sent to the delegate immediately upon starting the download.
- Zero or more [`download(_:willSend:redirectResponse:)`](./nsurldownloaddelegate/download%28_,willsend,redirectresponse%29.md) messages will be sent to the delegate before any further messages are sent if it is determined that the download must redirect to a new location. The delegate can allow the redirect, modify the destination or deny the redirect.
- Zero or more [`download(_:didReceive:)`](./nsurldownloaddelegate/download%28_,didreceive%29-1pc0v.md) messages will be sent to the delegate if it is necessary to authenticate in order to download the request and NSURLDownload does not already have authenticated credentials.
- Zero or more [`download(_:didCancel:)`](./nsurldownloaddelegate/download%28_,didcancel%29.md) messages will be sent to the delegate if [`NSURLDownload`](./nsurldownload.md) cancels the authentication challenge due to encountering a protocol implementation error.
- Zero or more [`download(_:didReceive:)`](./nsurldownloaddelegate/download%28_,didreceive%29-817z3.md) messages will be sent to the delegate before receiving a [`download(_:didReceiveDataOfLength:)`](./nsurldownloaddelegate/download%28_,didreceivedataoflength%29.md) message. The only case where [`download(_:didReceive:)`](./nsurldownloaddelegate/download%28_,didreceive%29-817z3.md) is not sent to a delegate is when the protocol implementation encounters an error before a response could be created.
- Zero or more [`download(_:didReceiveDataOfLength:)`](./nsurldownloaddelegate/download%28_,didreceivedataoflength%29.md) messages will be sent before [`downloadDidFinish(_:)`](./nsurldownloaddelegate/downloaddidfinish%28_%29.md) or [`download(_:didFailWithError:)`](./nsurldownloaddelegate/download%28_,didfailwitherror%29.md) is sent to the delegate.
- Zero or one [`download(_:decideDestinationWithSuggestedFilename:)`](./nsurldownloaddelegate/download%28_,decidedestinationwithsuggestedfilename%29.md) will be sent to the delegate when sufficient information has been received to determine the suggested filename for the downloaded file. The delegate will not receive this message if [`setDestination(_:allowOverwrite:)`](./nsurldownload/setdestination%28_,allowoverwrite%29.md) has already been sent to the [`NSURLDownload`](./nsurldownload.md) instance.
- A [`download(_:didCreateDestination:)`](./nsurldownloaddelegate/download%28_,didcreatedestination%29.md) message will be sent to the delegate when the [`NSURLDownload`](./nsurldownload.md) instance creates the file on disk.
- If NSURLDownload determines that the downloaded file is in a format that it is able to decode (MacBinary, Binhex or gzip), the delegate will receive a [`download(_:shouldDecodeSourceDataOfMIMEType:)`](./nsurldownloaddelegate/download%28_,shoulddecodesourcedataofmimetype%29.md). The delegate should return [`true`](../Swift/true.md) to decode the data, [`false`](../Swift/false.md) otherwise.
- Unless an [`NSURLDownload`](./nsurldownload.md) instance receives a [`cancel()`](./nsurldownload/cancel%28%29.md) message, the delegate will receive one and only one [`downloadDidFinish(_:)`](./nsurldownloaddelegate/downloaddidfinish%28_%29.md) or [`download(_:didFailWithError:)`](./nsurldownloaddelegate/download%28_,didfailwitherror%29.md) message, but never both. In addition, once either of these messages are sent, the delegate will receive no further messages for the given [`NSURLDownload`](./nsurldownload.md).

## Topics

### Download Authentication
- [func download(NSURLDownload, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./nsurldownloaddelegate/download%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func download(NSURLDownload, didCancel: URLAuthenticationChallenge)](./nsurldownloaddelegate/download%28_,didcancel%29.md)
  Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [func download(NSURLDownload, didReceive: URLAuthenticationChallenge)](./nsurldownloaddelegate/download%28_,didreceive%29-1pc0v.md)
  Sent when the URL download must authenticate a challenge in order to download the request.
- [func downloadShouldUseCredentialStorage(NSURLDownload) -> Bool](./nsurldownloaddelegate/downloadshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should consult the credential storage to authenticate the download.
### Download Data and Responses
- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](./nsurldownloaddelegate/download%28_,decidedestinationwithsuggestedfilename%29.md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func downloadDidBegin(NSURLDownload)](./nsurldownloaddelegate/downloaddidbegin%28_%29.md)
  Sent immediately after a download object begins a download.
- [func download(NSURLDownload, didCreateDestination: String)](./nsurldownloaddelegate/download%28_,didcreatedestination%29.md)
  Sent when the destination file is created.
- [func download(NSURLDownload, didReceive: URLResponse)](./nsurldownloaddelegate/download%28_,didreceive%29-817z3.md)
  Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [func download(NSURLDownload, didReceiveDataOfLength: Int)](./nsurldownloaddelegate/download%28_,didreceivedataoflength%29.md)
  Sent as a download object receives data incrementally.
- [func download(NSURLDownload, shouldDecodeSourceDataOfMIMEType: String) -> Bool](./nsurldownloaddelegate/download%28_,shoulddecodesourcedataofmimetype%29.md)
  Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [func download(NSURLDownload, willResumeWith: URLResponse, fromByte: Int64)](./nsurldownloaddelegate/download%28_,willresumewith,frombyte%29.md)
  Sent when a download object has received a response from the server after attempting to resume a download.
- [func download(NSURLDownload, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](./nsurldownloaddelegate/download%28_,willsend,redirectresponse%29.md)
  Sent when the download object determines that it must change URLs in order to continue loading a request.
### Download Completion
- [func download(NSURLDownload, didFailWithError: any Error)](./nsurldownloaddelegate/download%28_,didfailwitherror%29.md)
  Sent if the download fails or if an I/O error occurs when the file is written to disk.
- [func downloadDidFinish(NSURLDownload)](./nsurldownloaddelegate/downloaddidfinish%28_%29.md)
  Sent when a download object has completed downloading successfully and has written its results to disk.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### URL Download
- [class NSURLDownload](./nsurldownload.md)
  An object that downloads a resource asynchronously and saves the data to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate)*