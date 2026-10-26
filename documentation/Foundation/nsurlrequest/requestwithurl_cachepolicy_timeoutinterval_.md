# requestWithURL:cachePolicy:timeoutInterval:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an initialized URL request with specified URL, cache policy, and timeout values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) requestWithURL:(NSURL *) URL cachePolicy:(NSURLRequestCachePolicy) cachePolicy timeoutInterval:(NSTimeInterval) timeoutInterval;
```

#### Return Value

The initialized URL request.

## Parameters

- `URL`: The URL for the new request.
- `cachePolicy`: The cache policy for the new request.
- `timeoutInterval`: The timeout interval for the new request, in seconds.

## See Also

### Creating requests
- [+ requestWithURL:](./requestwithurl_.md)
  Creates and returns a URL request for a specified URL.
- [convenience init(url: URL)](./init%28url%29-7dmpd.md)
  Creates a URL request for a specified URL.
- [init(url: URL, cachePolicy: NSURLRequest.CachePolicy, timeoutInterval: TimeInterval)](./init%28url,cachepolicy,timeoutinterval%29-2giyj.md)
  Creates a URL request with the specified URL, cache policy, and timeout values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/requestwithurl:cachepolicy:timeoutinterval:)*