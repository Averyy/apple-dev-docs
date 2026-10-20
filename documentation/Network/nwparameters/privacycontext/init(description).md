# init(description:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a privacy context with a description string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(description: String)
```

## See Also

### Configuring Custom Privacy Settings
- [static let `default`: NWParameters.PrivacyContext](./default.md)
  The privacy context that applies to all connections that do not use a custom context.
- [func disableLogging()](./disablelogging%28%29.md)
  Disables system logging of connection activity.
- [func flushCache()](./flushcache%28%29.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/init(description:))*