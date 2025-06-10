# NSURLDownload

**Framework**: Foundation  
**Kind**: class

An object that downloads a resource asynchronously and saves the data to a file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class NSURLDownload
```

#### Overview

> ❗ **Important**:  This API is considered legacy. Use [`URLSession`](urlsession.md) instead.

The interface for [`NSURLDownload`](nsurldownload.md) provides methods to initialize a download, set the destination path and cancel loading the request.

The delegate object assigned to each instance of this class should implement the methods defined by the [`NSURLDownloadDelegate`](nsurldownloaddelegate.md) protocol. These methods provide the delegate with the current status of in-progress asynchronous downloads and allow the delegate to customize the URL loading process. These delegate methods are called on the thread that started the asynchronous load operation for the associated [`NSURLDownload`](nsurldownload.md) object.

## Topics

### Creating and configuring a download instance
- [init(request: URLRequest, delegate: (any NSURLDownloadDelegate)?)](nsurldownload/init(request:delegate:).md)
  Returns an initialized URL download for a URL request and begins to download the data for the request.
- [func setDestination(String, allowOverwrite: Bool)](nsurldownload/setdestination(_:allowoverwrite:).md)
  Sets the destination path of the downloaded file.
### Resuming partial downloads
- [class func canResumeDownloadDecoded(withEncodingMIMEType: String) -> Bool](nsurldownload/canresumedownloaddecoded(withencodingmimetype:).md)
  Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)](nsurldownload/init(resumedata:delegate:path:).md)
  Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.
- [var resumeData: Data?](nsurldownload/resumedata.md)
  Returns the resume data for a download that is not yet complete.
- [var deletesFileUponFailure: Bool](nsurldownload/deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.
### Canceling a download
- [func cancel()](nsurldownload/cancel.md)
  Cancels the receiver’s download and deletes the downloaded file.
### Getting download properties
- [var request: URLRequest](nsurldownload/request.md)
  Returns the request that initiated the receiver’s download.
- [var deletesFileUponFailure: Bool](nsurldownload/deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSURLDownloadDelegate](nsurldownloaddelegate.md)
  A protocol that URL download delegates implement to interact with a URL download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload)*