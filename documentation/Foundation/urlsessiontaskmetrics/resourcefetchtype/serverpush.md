# URLSessionTaskMetrics.ResourceFetchType.serverPush

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The resource was pushed by the server to the client.

**Availability**:
- iOS 10.0+ - Deprecated in 18.4
- iPadOS 10.0+ - Deprecated in 18.4
- Mac Catalyst 13.1+ - Deprecated in 18.4
- macOS 10.12+ - Deprecated in 15.4
- tvOS 10.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 3.0+ - Deprecated in 11.4

> **Deprecated**: Server push is no longer supported as of iOS 17 and aligned releases

## Declaration

```swift
case serverPush
```

```c
NSURLSessionTaskMetricsResourceFetchTypeServerPush
```

## See Also

### Fetch types
- [URLSessionTaskMetrics.ResourceFetchType.unknown](./unknown.md)
  The manner in which the resource was fetched could not be determined.
- [URLSessionTaskMetrics.ResourceFetchType.networkLoad](./networkload.md)
  The resource was loaded over the network.
- [URLSessionTaskMetrics.ResourceFetchType.localCache](./localcache.md)
  The resource was retrieved from the local storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/serverpush)*