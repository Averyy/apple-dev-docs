# acknowledge()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [`jobLimit`](../phassetresourceuploadjob/joblimit.md).

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func acknowledge()
```

```objc
- (void) acknowledge;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## See Also

### Processing jobs
- [func retry(destination: URLRequest?)](./retry%28destination%29.md)
  Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [`jobLimit`](../phassetresourceuploadjob/joblimit.md).
- [func cancel()](./cancel%28%29.md)
  Cancels an upload job that is registered or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/acknowledge())*