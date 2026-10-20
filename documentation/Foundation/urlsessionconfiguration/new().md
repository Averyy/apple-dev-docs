# new()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an empty session configuration.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: Use [`default`](./default.md) or other class methods to create instances.

## Declaration

```swift
class func new() -> Self
```

```objc
+ (instancetype) new;
```

## See Also

### Creating a session configuration object
- [class var `default`: URLSessionConfiguration](./default.md)
  A default session configuration object.
- [class var ephemeral: URLSessionConfiguration](./ephemeral.md)
  A session configuration that uses no persistent storage for caches, cookies, or credentials.
- [class func background(withIdentifier: String) -> URLSessionConfiguration](./background%28withidentifier%29.md)
  Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.
- [init()](./init%28%29.md)
  Creates an empty session configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/new())*