# default

**Framework**: Network  
**Kind**: property

The privacy context that applies to all connections that do not use a custom context.

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
static let `default`: NWParameters.PrivacyContext
```

#### Discussion

You cannot disable logging on the default privacy context.

Flushing the cache on the default privacy context will not affect other privacy contexts.

Changing name resolution settings will only affect privacy contexts that did not already explicitly configure resolution requirements.

## See Also

- [init(description: String)](nwparameters/privacycontext/init(description:).md)
  Initializes a privacy context with a description string.
- [func disableLogging()](nwparameters/privacycontext/disablelogging.md)
  Disables system logging of connection activity.
- [func flushCache()](nwparameters/privacycontext/flushcache.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/privacycontext/default)*