# currentPath

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The current evaluated path for the session’s [`resolvedEndpoint`](./resolvedendpoint.md) property.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_copy_current_path(_:)`](../../Network/nw_connection_copy_current_path%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var currentPath: NWPath? { get }
```

```objc
@property (nonatomic, readonly, nullable) NWPath * currentPath;
```

## Discussion

Use Key-Value Observing (KVO) to watch for changes to this property. For information about KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Getting session properties
- [var endpoint: NWEndpoint](./endpoint.md)
  The destination endpoint with which this session was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/currentpath)*