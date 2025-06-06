# NWPath

**Framework**: Network Extension  
**Kind**: class

The path made by a network connection, including information about its viability.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWPath
```

#### Overview

For example, if the path status is [`NWPathStatus.satisfied`](nwpathstatus/satisfied.md), then a connection attempt will be made.

When attached to a specific connection, a path takes all of the connection parameters into account. For example, if the route for a connection changes or is removed, the path will reflect that change. Note that every path is evaluated within the context of the process it is running in, and may be different across processes.

[`NWPath`](nwpath.md) is a static object, and properties of the path will never change. To monitor changing network status, use Key-Value Observing (KVO) to watch a path property on another object. For information about KVO, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Topics

### Getting network path properties
- [var status: NWPathStatus](nwpath/status.md)
  The evaluated status of the network path.
- [enum NWPathStatus](nwpathstatus.md)
- [var isExpensive: Bool](nwpath/isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.
- [var isConstrained: Bool](nwpath/isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.
### Comparing network paths
- [func isEqual(to: NWPath) -> Bool](nwpath/isequal(to:).md)
  Comparison method for [`NWPath`](nwpath.md) objects.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath)*