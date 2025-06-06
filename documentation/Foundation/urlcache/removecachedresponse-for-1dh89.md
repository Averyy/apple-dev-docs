# removeCachedResponse(for:)

**Framework**: Foundation  
**Kind**: method

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

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

If you override this method, you should also override [`removeCachedResponse(for:)`](urlcache/removecachedresponse(for:)-1zwp6.md).

## Parameters

- `request`: The URL request whose cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## See Also

- [func removeCachedResponse(for: URLSessionDataTask)](urlcache/removecachedresponse(for:)-1zwp6.md)
  Removes the cached URL response for a specified data task.
- [func removeCachedResponses(since: Date)](urlcache/removecachedresponses(since:).md)
  Clears the given cache of any cached responses since the provided date.
- [func removeAllCachedResponses()](urlcache/removeallcachedresponses.md)
  Clears the receiver’s cache, removing all stored cached URL responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1dh89)*