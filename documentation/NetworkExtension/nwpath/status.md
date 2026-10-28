# status

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The evaluated status of the network path.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_get_status(_:)`](../../Network/nw_path_get_status%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var status: NWPathStatus { get }
```

```objc
@property (nonatomic, readonly) NWPathStatus status;
```

## Discussion

The status of a path indicates whether or not the process is able to make connection attempts to any, or a specific, network endpoint. A satisfied status does not guarantee that a connection will be successful, but it does ensure that there is some interface over which an attempt can be made.

## See Also

### Getting network path properties
- [enum NWPathStatus](../nwpathstatus.md)
- [var isExpensive: Bool](./isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.
- [var isConstrained: Bool](./isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/status)*