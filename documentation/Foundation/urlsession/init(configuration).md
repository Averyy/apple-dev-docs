# init(configuration:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a session with the specified session configuration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(configuration: URLSessionConfiguration)
```

```objc
+ (NSURLSession *) sessionWithConfiguration:(NSURLSessionConfiguration *) configuration;
```

#### Discussion

Calling this method is equivalent to calling [`init(configuration:delegate:delegateQueue:)`](./init%28configuration,delegate,delegatequeue%29.md) with a `nil` delegate and queue.

## Parameters

- `configuration`: A configuration object that specifies certain behaviors, such as caching policies, timeouts, proxies, pipelining, TLS versions to support, cookie policies, credential storage, and so on.

  See [`URLSessionConfiguration`](../urlsessionconfiguration.md) for more information.

## See Also

### Creating a session
- [init(configuration: URLSessionConfiguration, delegate: (any URLSessionDelegate)?, delegateQueue: OperationQueue?)](./init%28configuration,delegate,delegatequeue%29.md)
  Creates a session with the specified session configuration, delegate, and operation queue.
- [class URLSessionConfiguration](../urlsessionconfiguration.md)
  A configuration object that defines behavior and policies for a URL session.
- [var configuration: URLSessionConfiguration](./configuration.md)
  A copy of the configuration object for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/init(configuration:))*