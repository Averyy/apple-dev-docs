# storeCachedResponse(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) storeCachedResponse:(NSCachedURLResponse *) cachedResponse forDataTask:(NSURLSessionDataTask *) dataTask;
```

## Parameters

- `cachedResponse`: The cached URL response to store for this data task.
- `dataTask`: The data task whose response is to be cached.

## See Also

### Getting and storing cached objects
- [func cachedResponse(for: URLRequest) -> CachedURLResponse?](./cachedresponse%28for%29.md)
  Returns the cached URL response in the cache for the specified URL request.
- [func storeCachedResponse(CachedURLResponse, for: URLRequest)](./storecachedresponse%28_,for%29-7p7bl.md)
  Stores a cached URL response for a specified request.
- [func getCachedResponse(for: URLSessionDataTask, completionHandler: (CachedURLResponse?) -> Void)](./getcachedresponse%28for,completionhandler%29.md)
  Gets the cached URL response for a data task, passing it to the provided completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/storecachedresponse(_:for:)-8uq91)*