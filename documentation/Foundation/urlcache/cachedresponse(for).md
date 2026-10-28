# cachedResponse(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSCachedURLResponse *) cachedResponseForRequest:(NSURLRequest *) request;
```

## Mentions

- [Accessing cached data](../accessing-cached-data.md)

## Return Value

The cached URL response for `request`, or `nil` if no response has been cached.

## Discussion

If you override this method, you should also override [`getCachedResponse(for:completionHandler:)`](./getcachedresponse%28for,completionhandler%29.md).

## Parameters

- `request`: The URL request whose cached response is desired.

## See Also

### Getting and storing cached objects
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](./storecachedresponse%28_,for%29-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](./getcachedresponse%28for,completionhandler%29.md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](./storecachedresponse%28_,for%29-8uq91.md)
  Stores a cached URL response for a specified data task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/cachedresponse(for:))*