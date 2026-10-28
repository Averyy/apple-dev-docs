# NWPath

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The path made by a network connection, including information about its viability.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_t`](../Network/nw_path_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
class NWPath
```

```objc
@interface NWPath : NSObject
```

## Overview

For example, if the path status is [`NWPathStatus.satisfied`](./nwpathstatus/satisfied.md), then a connection attempt will be made.

When attached to a specific connection, a path takes all of the connection parameters into account. For example, if the route for a connection changes or is removed, the path will reflect that change. Note that every path is evaluated within the context of the process it is running in, and may be different across processes.

[`NWPath`](./nwpath.md) is a static object, and properties of the path will never change. To monitor changing network status, use Key-Value Observing (KVO) to watch a path property on another object. For information about KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Topics

### Getting network path properties
- [var status: NWPathStatus](./nwpath/status.md)
  The evaluated status of the network path.
- [enum NWPathStatus](./nwpathstatus.md)
- [var isExpensive: Bool](./nwpath/isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.
- [var isConstrained: Bool](./nwpath/isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.
### Comparing network paths
- [func isEqual(to: NWPath) -> Bool](./nwpath/isequal%28to%29.md)
  Comparison method for [`NWPath`](./nwpath.md) objects.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath)*