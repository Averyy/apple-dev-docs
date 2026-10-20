# setDestination(_:allowOverwrite:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the destination path of the downloaded file.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func setDestination(_ path: String, allowOverwrite: Bool)
```

```objc
- (void) setDestination:(NSString *) path allowOverwrite:(BOOL) allowOverwrite;
```

#### Discussion

If `allowOverwrite` is [`false`](../../Swift/false.md) and a file already exists at `path`, a unique filename will be created for the downloaded file by appending a number to the filename. The delegate can implement the [`download(_:didCreateDestination:)`](../nsurldownloaddelegate/download%28_,didcreatedestination%29.md) delegate method to determine the filename used when the file is written to disk.

##### Special Considerations

An `NSURLDownload` instance ignores multiple calls to this method.

## Parameters

- `path`: The path for the downloaded file.
- `allowOverwrite`: [`true`](../../Swift/true.md) if an existing file at `path` can be replaced, [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [func download(NSURLDownload, decideDestinationWithSuggestedFilename: String)](../nsurldownloaddelegate/download%28_,decidedestinationwithsuggestedfilename%29.md)
  The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [func download(NSURLDownload, didCreateDestination: String)](../nsurldownloaddelegate/download%28_,didcreatedestination%29.md)
  Sent when the destination file is created.
### Creating and configuring a download instance
- [init(request: URLRequest, delegate: (any NSURLDownloadDelegate)?)](./init%28request,delegate%29.md)
  Returns an initialized URL download for a URL request and begins to download the data for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/setdestination(_:allowoverwrite:))*