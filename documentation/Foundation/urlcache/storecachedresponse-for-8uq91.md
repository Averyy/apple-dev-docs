# storeCachedResponse(_:for:)

**Framework**: Foundation  
**Kind**: method

Stores a cached URL response for a specified data task.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func storeCachedResponse(_ cachedResponse: CachedURLResponse, for dataTask: URLSessionDataTask)
```

## Parameters

- `cachedResponse`: The cached URL response to store for this data task.
- `dataTask`: The data task whose response is to be cached.

## See Also

- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](urlcache/cachedresponse(for:).md)
  Returns the cached URL response in the cache for the specified URL request.
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](urlcache/storecachedresponse(_:for:)-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](urlcache/getcachedresponse(for:completionhandler:).md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storecachedresponse(_:for:)-8uq91)*