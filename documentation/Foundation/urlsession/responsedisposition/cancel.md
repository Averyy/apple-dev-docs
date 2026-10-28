# URLSession.ResponseDisposition.cancel

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

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

```c
NSURLSessionResponseCancel
```

## Discussion

Using this disposition is equivalent to calling [`cancel()`](../../urlsessiontask/cancel%28%29.md) on the task.

## See Also

### Task dispositions
- [URLSession.ResponseDisposition.allow](./allow.md)
  Allow the load operation to continue.
- [URLSession.ResponseDisposition.becomeDownload](./becomedownload.md)
  Convert the response for this request to use a [`URLSessionDownloadTask`](../../urlsessiondownloadtask.md).
- [URLSession.ResponseDisposition.becomeStream](./becomestream.md)
  Convert the response for this request to use a [`URLSessionStreamTask`](../../urlsessionstreamtask.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/cancel)*