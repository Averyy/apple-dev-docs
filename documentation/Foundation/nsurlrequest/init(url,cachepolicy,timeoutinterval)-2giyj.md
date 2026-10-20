# init(url:cachePolicy:timeoutInterval:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL request with the specified URL, cache policy, and timeout values.

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
init(url URL: URL, cachePolicy: NSURLRequest.CachePolicy, timeoutInterval: TimeInterval)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL cachePolicy:(NSURLRequestCachePolicy) cachePolicy timeoutInterval:(NSTimeInterval) timeoutInterval;
```

#### Return Value

The initialized URL request.

#### Discussion

This is the designated initializer for `NSURLRequest`.

## Parameters

- `URL`: The URL for the request.
- `cachePolicy`: The cache policy for the request.
- `timeoutInterval`: The timeout interval for the request, in seconds.

## See Also

### Creating requests
- [convenience init(url: URL)](./init%28url%29-7dmpd.md)
  Creates a URL request for a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/init(url:cachepolicy:timeoutinterval:)-2giyj)*