# isExpensive

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the path uses an expensive interface.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_is_expensive(_:)`](../../Network/nw_path_is_expensive%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var isExpensive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isExpensive) BOOL expensive;
```

#### Discussion

Returns YES is the path uses an interface that is considered expensive, such as when using a cellular data plan.

## See Also

### Getting network path properties
- [var status: NWPathStatus](./status.md)
  The evaluated status of the network path.
- [enum NWPathStatus](../nwpathstatus.md)
- [var isConstrained: Bool](./isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/isexpensive)*