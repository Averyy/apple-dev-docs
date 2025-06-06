# cachePolicy

**Framework**: Foundation  
**Kind**: property

The request’s cache policy.

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
var cachePolicy: NSURLRequest.CachePolicy { get set }
```

#### Discussion

This property is ignored for requests used to construct [`URLSessionUploadTask`](urlsessionuploadtask.md) and [`URLSessionDownloadTask`](urlsessiondownloadtask.md) objects, as caching is not supported by the URL Loading System for upload or download requests.

## See Also

- [NSURLRequest.CachePolicy](nsurlrequest/cachepolicy-swift.enum.md)
  The constants used to specify interaction with the cached responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/cachepolicy)*