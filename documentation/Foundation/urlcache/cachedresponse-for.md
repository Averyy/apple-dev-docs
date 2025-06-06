# cachedResponse(for:)

**Framework**: Foundation  
**Kind**: method

Returns the cached URL response in the cache for the specified URL request.

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
func cachedResponse(for request: URLRequest) -> CachedURLResponse?
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Return Value

The cached URL response for `request`, or `nil` if no response has been cached.

#### Discussion

If you override this method, you should also override [`getCachedResponse(for:completionHandler:)`](urlcache/getcachedresponse(for:completionhandler:).md).

## Parameters

- `request`: The URL request whose cached response is desired.

## See Also

- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](urlcache/storecachedresponse(_:for:)-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](urlcache/getcachedresponse(for:completionhandler:).md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](urlcache/storecachedresponse(_:for:)-8uq91.md)
  Stores a cached URL response for a specified data task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/cachedresponse(for:))*