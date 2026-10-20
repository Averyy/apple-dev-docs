# getCachedResponse(for:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func getCachedResponse(for dataTask: URLSessionDataTask, completionHandler: @escaping @Sendable (CachedURLResponse?) -> Void)
```

```swift
func cachedResponse(for dataTask: URLSessionDataTask) async -> CachedURLResponse?
```

```objc
- (void) getCachedResponseForDataTask:(NSURLSessionDataTask *) dataTask completionHandler:(void (^)(NSCachedURLResponse *cachedResponse)) completionHandler;
```

## Parameters

- `dataTask`: The data task whose cached URL response is desired.
- `completionHandler`: A completion handler that receives the cached URL response for the data task’s request, or `nil` if no response is found in the cache.

## See Also

### Getting and storing cached objects
- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](./cachedresponse%28for%29.md)
  Returns the cached URL response in the cache for the specified URL request.
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](./storecachedresponse%28_,for%29-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func storeCachedResponse(CachedURLResponse, for: URLSessionDataTask)](./storecachedresponse%28_,for%29-8uq91.md)
  Stores a cached URL response for a specified data task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/getcachedresponse(for:completionhandler:))*