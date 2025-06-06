# init(configuration:)

**Framework**: Foundation  
**Kind**: init

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

#### Discussion

Calling this method is equivalent to calling [`init(configuration:delegate:delegateQueue:)`](urlsession/init(configuration:delegate:delegatequeue:).md) with a `nil` delegate and queue.

## Parameters

- `configuration`: See   for more information.

## See Also

- [init(configuration: URLSessionConfiguration, delegate: (any URLSessionDelegate)?, delegateQueue: OperationQueue?)](urlsession/init(configuration:delegate:delegatequeue:).md)
  Creates a session with the specified session configuration, delegate, and operation queue.
- [class URLSessionConfiguration](urlsessionconfiguration.md)
  A configuration object that defines behavior and policies for a URL session.
- [var configuration: URLSessionConfiguration](urlsession/configuration.md)
  A copy of the configuration object for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/init(configuration:))*