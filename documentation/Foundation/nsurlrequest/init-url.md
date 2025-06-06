# init(url:)

**Framework**: Foundation  
**Kind**: init

Creates a URL request for a specified URL.

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
convenience init(url URL: URL)
```

#### Return Value

The initialized URL request.

#### Discussion

The request is created with the with the default cache policy ([`NSURLRequest.CachePolicy.useProtocolCachePolicy`](nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md)), and the default timeout interval (60 seconds).

## Parameters

- `URL`: The URL for the request.

## See Also

- [init(url: URL, cachePolicy: NSURLRequest.CachePolicy, timeoutInterval: TimeInterval)](nsurlrequest/init(url:cachepolicy:timeoutinterval:).md)
  Creates a URL request with the specified URL, cache policy, and timeout values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/init(url:))*