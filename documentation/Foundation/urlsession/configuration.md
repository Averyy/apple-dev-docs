# configuration

**Framework**: Foundation  
**Kind**: property

A copy of the configuration object for this session.

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
@NSCopying
var configuration: URLSessionConfiguration { get }
```

## Mentions

- [Accessing cached data](accessing-cached-data.md)

#### Discussion

Beginning in iOS 9 and OS X 10.11, [`URLSession`](urlsession.md) objects store a copy of the [`URLSessionConfiguration`](urlsessionconfiguration.md) object passed to their initializers, such that a session’s configuration is immutable after initialization. Any further changes to mutable properties on the configuration object passed to a session’s initializer or the value returned from a session’s configuration property do not affect the behavior of that session. However, you can create a new session with the modified configuration object.

> **Note**:  On previous versions of iOS and macOS, a bug in the implementation causes [`URLSession`](urlsession.md) objects to store a  to configuration objects passed to their initializers rather than a copy. This allows the behavior of a session to be further configured after initialization by modifying the configuration object passed to a session’s initializer or the value returned from a session’s [`configuration`](urlsession/configuration.md) property. You can ensure consistent behavior across different platform versions by explicitly calling [`copy()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copy()) on configuration objects passed to a [`URLSession`](urlsession.md) initializer or returned from the [`configuration`](urlsession/configuration.md) property.

## See Also

- [init(configuration: URLSessionConfiguration)](urlsession/init(configuration:).md)
  Creates a session with the specified session configuration.
- [init(configuration: URLSessionConfiguration, delegate: (any URLSessionDelegate)?, delegateQueue: OperationQueue?)](urlsession/init(configuration:delegate:delegatequeue:).md)
  Creates a session with the specified session configuration, delegate, and operation queue.
- [class URLSessionConfiguration](urlsessionconfiguration.md)
  A configuration object that defines behavior and policies for a URL session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/configuration)*