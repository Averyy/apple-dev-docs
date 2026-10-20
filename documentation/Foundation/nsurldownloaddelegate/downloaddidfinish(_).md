# downloadDidFinish(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when a download object has completed downloading successfully and has written its results to disk.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func downloadDidFinish(_ download: NSURLDownload)
```

```objc
- (void) downloadDidFinish:(NSURLDownload *) download;
```

#### Discussion

The delegate will receive no further messages for `download`.

## Parameters

- `download`: The URL download object sending the message.

## See Also

### Download Completion
- [func download(NSURLDownload, didFailWithError: any Error)](./download%28_,didfailwitherror%29.md)
  Sent if the download fails or if an I/O error occurs when the file is written to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/downloaddidfinish(_:))*