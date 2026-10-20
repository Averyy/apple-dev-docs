# isConstrained

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_is_constrained(_:)`](../../Network/nw_path_is_constrained%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var isConstrained: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isConstrained) BOOL constrained;
```

## See Also

### Getting network path properties
- [var status: NWPathStatus](./status.md)
  The evaluated status of the network path.
- [enum NWPathStatus](../nwpathstatus.md)
- [var isExpensive: Bool](./isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/isconstrained)*