# ephemeral

**Framework**: Foundation  
**Kind**: property

A session configuration that uses no persistent storage for caches, cookies, or credentials.

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
class var ephemeral: URLSessionConfiguration { get }
```

#### Discussion

An ephemeral session configuration object is similar to a default session configuration (see [`default`](urlsessionconfiguration/default.md)), except that the corresponding session object doesn’t store caches, credential stores, or any session-related data to disk. Instead, session-related data is stored in RAM. The only time an ephemeral session writes data to disk is when you tell it to write the contents of a URL to a file.

> **Note**:  It is possible to customize a default session configuration object to obtain the same behavior (or any portion thereof) provided by an ephemeral session configuration object, but the use of this method is more convenient.

##### Privacy and Performance Considerations

The main advantage to using ephemeral sessions is privacy. By not writing potentially sensitive data to disk, you make it less likely that the data will be intercepted and used later. For this reason, ephemeral sessions are ideal for private browsing modes in web browsers and other similar situations.

Because an ephemeral session doesn’t write cached data to disk, the size of the cache is limited by available RAM. This limitation means that previously fetched resources are less likely to be in the cache (and are guaranteed to not be there if the user quits and relaunches your app). This behavior may reduce perceived performance, depending on your app.

When your app invalidates the session, all ephemeral session data is purged automatically. Additionally, in iOS, the in-memory cache isn’t purged automatically when your app is suspended but may be purged when your app is terminated or when the system experiences memory pressure.

## See Also

- [var isDiscretionary: Bool](urlsessionconfiguration/isdiscretionary.md)
  A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.
- [class var `default`: URLSessionConfiguration](urlsessionconfiguration/default.md)
  A default session configuration object.
- [class func background(withIdentifier: String) -> URLSessionConfiguration](urlsessionconfiguration/background(withidentifier:).md)
  Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.
- [init()](urlsessionconfiguration/init.md)
  Creates an empty session configuration.
- [class func new() -> Self](urlsessionconfiguration/new.md)
  Creates an empty session configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/ephemeral)*