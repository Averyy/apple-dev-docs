# storeCachedResponse(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Stores a cached URL response for a specified request.

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
func storeCachedResponse(_ cachedResponse: CachedURLResponse, for request: URLRequest)
```

```objc
- (void) storeCachedResponse:(NSCachedURLResponse *) cachedResponse forRequest:(NSURLRequest *) request;
```

## Mentions

- [Accessing cached data](../accessing-cached-data.md)

#### Discussion

If you override this method, you should also override [`storeCachedResponse(_:for:)`](./storecachedresponse%28_,for%29-8uq91.md).

## Parameters

- `cachedResponse`: The cached URL response to store.
- `request`: The request for which the cached URL response is being stored.

## See Also

### Getting and storing cached objects
- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](./cachedresponse%28for%29.md)
  Returns the cached URL response in the cache for the specified URL request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](./getcachedresponse%28for,completionhandler%29.md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](./storecachedresponse%28_,for%29-8uq91.md)
  Stores a cached URL response for a specified data task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storecachedresponse(_:for:)-7p7bl)*