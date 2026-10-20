# flushCache()

**Framework**: Network  
**Kind**: method

Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

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
func flushCache()
```

#### Discussion

Flushing the cache may be asynchronous, which means that it will take effect shortly after you invoke the function.

## See Also

- [init(description: String)](nwparameters/privacycontext/init(description:).md)
  Initializes a privacy context with a description string.
- [static let `default`: NWParameters.PrivacyContext](nwparameters/privacycontext/default.md)
  The privacy context that applies to all connections that do not use a custom context.
- [func disableLogging()](nwparameters/privacycontext/disablelogging.md)
  Disables system logging of connection activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/flushcache())*