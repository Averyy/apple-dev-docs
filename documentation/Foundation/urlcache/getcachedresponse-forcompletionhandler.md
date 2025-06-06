# getCachedResponse(for:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Gets the cached URL response for a data task, passing it to the provided completion handler.

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
func cachedResponse(for dataTask: URLSessionDataTask) async -> CachedURLResponse?
```

## Parameters

- `dataTask`: The data task whose cached URL response is desired.
- `completionHandler`: A completion handler that receives the cached URL response for the data task’s request, or   if no response is found in the cache.

## See Also

- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](urlcache/cachedresponse(for:).md)
  Returns the cached URL response in the cache for the specified URL request.
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](urlcache/storecachedresponse(_:for:)-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](urlcache/storecachedresponse(_:for:)-8uq91.md)
  Stores a cached URL response for a specified data task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/getcachedresponse(for:completionhandler:))*