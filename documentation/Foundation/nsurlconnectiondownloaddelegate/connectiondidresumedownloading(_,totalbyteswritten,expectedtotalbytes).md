# connectionDidResumeDownloading(_:totalBytesWritten:expectedTotalBytes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when an URL connection resumes downloading a URL asset that was earlier suspended.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func connectionDidResumeDownloading(_ connection: NSURLConnection, totalBytesWritten: Int64, expectedTotalBytes: Int64)
```

```objc
- (void) connectionDidResumeDownloading:(NSURLConnection *) connection totalBytesWritten:(long long) totalBytesWritten expectedTotalBytes:(long long) expectedTotalBytes;
```

#### Discussion

This method is invoked once a suspended download of a URL asset resumes downloading. In response, the delegate can display a progress indicator, setting the initial value of the indicator to where it was when downloading was suspended. After the URL-connection object sends this message, it sends one or more [`connection(_:didWriteData:totalBytesWritten:expectedTotalBytes:)`](./connection%28_,didwritedata,totalbyteswritten,expectedtotalbytes%29.md) to the delegate until the download concludes.

## Parameters

- `connection`: The URL connection object downloading the asset.
- `totalBytesWritten`: The total number of bytes of the downloading asset that have been written to the destination file.
- `expectedTotalBytes`: The total number of bytes of the URL asset once it is completely downloaded and written to a file.

## See Also

### Managing Downloads of URL Assets
- [func connection(NSURLConnection, didWriteData: Int64, totalBytesWritten: Int64, expectedTotalBytes: Int64)](./connection%28_,didwritedata,totalbyteswritten,expectedtotalbytes%29.md)
  Sent to the delegate to deliver progress information for a download of a URL asset to a destination file.
- [func connectionDidFinishDownloading(NSURLConnection, destinationURL: URL)](./connectiondidfinishdownloading%28_,destinationurl%29.md)
  Sent to the delegate when the URL connection has successfully downloaded the URL asset to a destination file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidresumedownloading(_:totalbyteswritten:expectedtotalbytes:))*