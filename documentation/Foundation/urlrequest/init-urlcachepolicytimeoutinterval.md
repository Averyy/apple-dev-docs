# init(url:cachePolicy:timeoutInterval:)

**Framework**: Foundation  
**Kind**: init

Creates and initializes a URL request with the given URL, cache policy, and timeout interval.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(url: URL, cachePolicy: URLRequest.CachePolicy = .useProtocolCachePolicy, timeoutInterval: TimeInterval = 60.0)
```

## Parameters

- `url`: The URL for the request.
- `cachePolicy`: The cache policy for the request. The default is  .
- `timeoutInterval`: The timeout interval for the request. The default is  . See the commentary for the   for more information on timeout intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/init(url:cachepolicy:timeoutinterval:))*