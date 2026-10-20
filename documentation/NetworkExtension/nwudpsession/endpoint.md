# endpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The destination endpoint with which this session was created.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_copy_endpoint(_:)`](../../Network/nw_connection_copy_endpoint%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var endpoint: NWEndpoint { get }
```

```objc
@property (atomic, readonly) NWEndpoint * endpoint;
```

## See Also

### Getting session properties
- [var currentPath: NWPath?](./currentpath.md)
  The current evaluated path for the session’s [`resolvedEndpoint`](./resolvedendpoint.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/endpoint)*