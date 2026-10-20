# removeCachedResponse(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the cached URL response for a specified URL request.

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
func removeCachedResponse(for request: URLRequest)
```

```objc
- (void) removeCachedResponseForRequest:(NSURLRequest *) request;
```

## Mentions

- [Accessing cached data](../accessing-cached-data.md)

#### Discussion

If you override this method, you should also override [`removeCachedResponse(for:)`](./removecachedresponse%28for%29-1zwp6.md).

## Parameters

- `request`: The URL request whose cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## See Also

### Removing cached objects
- [func removeCachedResponse(for: URLSessionDataTask)](./removecachedresponse%28for%29-1zwp6.md)
  Removes the cached URL response for a specified data task.
- [func removeCachedResponses(since: Date)](./removecachedresponses%28since%29.md)
  Clears the given cache of any cached responses since the provided date.
- [func removeAllCachedResponses()](./removeallcachedresponses%28%29.md)
  Clears the receiver’s cache, removing all stored cached URL responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1dh89)*