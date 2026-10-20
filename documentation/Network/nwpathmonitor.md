# NWPathMonitor

**Framework**: Network  
**Kind**: class  
**Role**: Class

An observer that you use to monitor and react to network changes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final class NWPathMonitor
```

## Topics

### Creating Path Monitors
- [init()](./nwpathmonitor/init%28%29.md)
  Initializes a path monitor to observe all available interface types.
- [init(requiredInterfaceType: NWInterface.InterfaceType)](./nwpathmonitor/init%28requiredinterfacetype%29.md)
  Initializes a path monitor to observe a specific interface type.
- [init(prohibitedInterfaceTypes: [NWInterface.InterfaceType])](./nwpathmonitor/init%28prohibitedinterfacetypes%29.md)
  Initializes a path monitor to observe interface types that are not explicitly prohibited.
- [func start(queue: DispatchQueue)](./nwpathmonitor/start%28queue%29.md)
  Starts monitoring path changes, and sets a queue on which to deliver path events.
- [var queue: DispatchQueue?](./nwpathmonitor/queue.md)
  The queue on which path events are delivered.
### Handling Path Updates
- [var currentPath: NWPath](./nwpathmonitor/currentpath.md)
  The currently available network path observed by the path monitor.
- [var pathUpdateHandler: ((NWPath) -> Void)?](./nwpathmonitor/pathupdatehandler.md)
  A handler that receives network path updates.
### Canceling Path Monitors
- [func cancel()](./nwpathmonitor/cancel%28%29.md)
  Stops receiving network path updates.
### Structures
- [NWPathMonitor.Iterator](./nwpathmonitor/iterator.md)
### Type Properties
- [static var ethernetChannel: NWPathMonitor](./nwpathmonitor/ethernetchannel.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/asyncsequence.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Paths and Interfaces
- [struct NWPath](./nwpath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [struct NWInterface](./nwinterface.md)
  An interface that a network connection uses to send and receive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpathmonitor)*