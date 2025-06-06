# removeCachedResponses(since:)

**Framework**: Foundation  
**Kind**: method

Clears the given cache of any cached responses since the provided date.

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
func removeCachedResponses(since date: Date)
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

## Parameters

- `date`: The earliest date of responses that should remain in the cache. Any responses with dates later than this parameter should be removed.

## See Also

- [func removeCachedResponse(for: URLRequest)](urlcache/removecachedresponse(for:)-1dh89.md)
  Removes the cached URL response for a specified URL request.
- [func removeCachedResponse(for: URLSessionDataTask)](urlcache/removecachedresponse(for:)-1zwp6.md)
  Removes the cached URL response for a specified data task.
- [func removeAllCachedResponses()](urlcache/removeallcachedresponses.md)
  Clears the receiver’s cache, removing all stored cached URL responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcache/removecachedresponses(since:))*