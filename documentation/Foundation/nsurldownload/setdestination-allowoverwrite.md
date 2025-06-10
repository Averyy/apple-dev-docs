# setDestination(_:allowOverwrite:)

**Framework**: Foundation  
**Kind**: method

Sets the destination path of the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func setDestination(_ path: String, allowOverwrite: Bool)
```

#### Discussion

If `allowOverwrite` is [`false`](https://developer.apple.com/documentation/swift/false) and a file already exists at `path`, a unique filename will be created for the downloaded file by appending a number to the filename. The delegate can implement the [`download(_:didCreateDestination:)`](nsurldownloaddelegate/download(_:didcreatedestination:).md) delegate method to determine the filename used when the file is written to disk.

##### Special Considerations

An `NSURLDownload` instance ignores multiple calls to this method.

## Parameters

- `path`: The path for the downloaded file.
- `allowOverwrite`:   if an existing file at   can be replaced,   otherwise.

## See Also

- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:).md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func download(NSURLDownload, didCreateDestination: String)](nsurldownloaddelegate/download(_:didcreatedestination:).md)
  Sent when the destination file is created.
- [init(request: URLRequest, delegate: (any NSURLDownloadDelegate)?)](nsurldownload/init(request:delegate:).md)
  Returns an initialized URL download for a URL request and begins to download the data for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/setdestination(_:allowoverwrite:))*