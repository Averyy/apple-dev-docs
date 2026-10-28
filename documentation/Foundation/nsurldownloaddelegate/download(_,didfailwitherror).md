# download(_:didFailWithError:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent if the download fails or if an I/O error occurs when the file is written to disk.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didFailWithError error: any Error)
```

```objc
- (void) download:(NSURLDownload *) download didFailWithError:(NSError *) error;
```

## Discussion

Any partially downloaded file will be deleted.

### Special Considerations

Once the delegate receives this message, it will receive no further messages for `download`.

## Parameters

- `download`: The URL download object sending the message.
- `error`: The error that caused the failure of the download.

## See Also

### Download Completion
- [func downloadDidFinish(NSURLDownload)](./downloaddidfinish%28_%29.md)
  Sent when a download object has completed downloading successfully and has written its results to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didfailwitherror:))*