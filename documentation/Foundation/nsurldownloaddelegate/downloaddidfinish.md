# downloadDidFinish(_:)

**Framework**: Foundation  
**Kind**: method

Sent when a download object has completed downloading successfully and has written its results to disk.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func downloadDidFinish(_ download: NSURLDownload)
```

#### Discussion

The delegate will receive no further messages for `download`.

## Parameters

- `download`: The URL download object sending the message.

## See Also

- [func download(NSURLDownload, didFailWithError: any Error)](nsurldownloaddelegate/download(_:didfailwitherror:).md)
  Sent if the download fails or if an I/O error occurs when the file is written to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/downloaddidfinish(_:))*