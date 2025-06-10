# URLSession.ResponseDisposition.cancel

**Framework**: Foundation  
**Kind**: case

Cancel the load.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case cancel
```

#### Discussion

Using this disposition is equivalent to calling [`cancel()`](urlsessiontask/cancel().md) on the task.

## See Also

- [URLSession.ResponseDisposition.allow](urlsession/responsedisposition/allow.md)
  Allow the load operation to continue.
- [URLSession.ResponseDisposition.becomeDownload](urlsession/responsedisposition/becomedownload.md)
  Convert the response for this request to use a [`URLSessionDownloadTask`](urlsessiondownloadtask.md).
- [URLSession.ResponseDisposition.becomeStream](urlsession/responsedisposition/becomestream.md)
  Convert the response for this request to use a [`URLSessionStreamTask`](urlsessionstreamtask.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/cancel)*