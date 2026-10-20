# removeCachedResponse(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the cached URL response for a specified data task.

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
func removeCachedResponse(for dataTask: URLSessionDataTask)
```

```objc
- (void) removeCachedResponseForDataTask:(NSURLSessionDataTask *) dataTask;
```

## Parameters

- `dataTask`: A task whose URL request’s corresponding cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## See Also

### Removing cached objects
- [func removeCachedResponse(for: URLRequest)](./removecachedresponse%28for%29-1dh89.md)
  Removes the cached URL response for a specified URL request.
- [func removeCachedResponses(since: Date)](./removecachedresponses%28since%29.md)
  Clears the given cache of any cached responses since the provided date.
- [func removeAllCachedResponses()](./removeallcachedresponses%28%29.md)
  Clears the receiver’s cache, removing all stored cached URL responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1zwp6)*