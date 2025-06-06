# removeCachedResponse(for:)

**Framework**: Foundation  
**Kind**: method

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

## Parameters

- `dataTask`: A task whose URL request’s corresponding cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## See Also

- [func removeCachedResponse(for: URLRequest)](urlcache/removecachedresponse(for:)-1dh89.md)
  Removes the cached URL response for a specified URL request.
- [func removeCachedResponses(since: Date)](urlcache/removecachedresponses(since:).md)
  Clears the given cache of any cached responses since the provided date.
- [func removeAllCachedResponses()](urlcache/removeallcachedresponses.md)
  Clears the receiver’s cache, removing all stored cached URL responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1zwp6)*