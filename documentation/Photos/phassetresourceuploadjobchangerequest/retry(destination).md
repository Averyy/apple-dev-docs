# retry(destination:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Retries a job that is failed, unacknowledged, and has not been retried before. Successful retries also free up space for [`jobLimit`](../phassetresourceuploadjob/joblimit.md).

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func retry(destination: URLRequest?)
```

```objc
- (void) retryWithDestination:(NSURLRequest *) destination;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## See Also

### Processing jobs
- [func acknowledge()](./acknowledge%28%29.md)
  Acknowledges a successful or failed job. Jobs must be acknowledged to free up space for [`jobLimit`](../phassetresourceuploadjob/joblimit.md).
- [func cancel()](./cancel%28%29.md)
  Cancels an upload job that is registered or pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/retry(destination:))*