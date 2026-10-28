# LayerHierarchyHostingTransactionCoordinator

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A class that synchronizes updates to views and layers in different processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class LayerHierarchyHostingTransactionCoordinator
```

```objc
@interface BELayerHierarchyHostingTransactionCoordinator : NSObject
```

## Mentions

- [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md)

## Overview

Updates to your app’s UI occur through Core Animation’s underlying transaction mechanism. This class works with Core Animation to synchronize transactions that occur across processes in your browser app. To do that:

- Add views and layer hierarchies to an instance of this class.
- Share the instance between processes using [`createXPCRepresentation()`](./layerhierarchyhostingtransactioncoordinator/createxpcrepresentation%28%29.md) and [`init(xpcRepresentation:)`](./layerhierarchyhostingtransactioncoordinator/init%28xpcrepresentation%29.md), or [`encode(_:)`](./layerhierarchyhostingtransactioncoordinator/encode%28_%29.md) and [`init(port:data:)`](./layerhierarchyhostingtransactioncoordinator/init%28port,data%29.md).
- Perform the necessary Core Animation transactions.
- Call [`commit()`](./layerhierarchyhostingtransactioncoordinator/commit%28%29.md) on the instance, and discard it.

For more information, see [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md).

## Topics

### Creating a transaction coordinator
- [init() throws](./layerhierarchyhostingtransactioncoordinator/init%28%29.md)
  Creates a transaction coordinator.
- [init?(coder: NSCoder)](./layerhierarchyhostingtransactioncoordinator/init%28coder%29.md)
  Creates a transaction coordinator from an encoded representation.
### Sharing a transaction coordinator using XPC
- [func createXPCRepresentation() -> xpc_object_t](./layerhierarchyhostingtransactioncoordinator/createxpcrepresentation%28%29.md)
  Creates a representation of the transaction coordinator that you send to another process.
- [init(xpcRepresentation: xpc_object_t?) throws](./layerhierarchyhostingtransactioncoordinator/init%28xpcrepresentation%29.md)
  Creates a transaction coordinator from an XPC object.
### Sharing a transaction coordinator using Mach
- [func encode((mach_port_t, Data) -> Void)](./layerhierarchyhostingtransactioncoordinator/encode%28_%29.md)
  Serializes the transaction coordinator into a Mach port reference and accompanying data.
- [init(port: mach_port_t, data: Data) throws](./layerhierarchyhostingtransactioncoordinator/init%28port,data%29.md)
  Creates a transaction coordinator using a Mach port reference and serialized data.
### Synchronizing transactions
- [func add(LayerHierarchyHostingView)](./layerhierarchyhostingtransactioncoordinator/add%28_%29-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func add(LayerHierarchy)](./layerhierarchyhostingtransactioncoordinator/add%28_%29-i66q.md)
  Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.
- [func commit()](./layerhierarchyhostingtransactioncoordinator/commit%28%29.md)
  Notifies the render server to coordinate transactions for the added views and layer hierarchies.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Layer hosting
- [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](./layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingView](./layerhierarchyhostingview.md)
  A view that hosts a layer hierarchy you manage in another process.
- [class LayerHierarchyHandle](./layerhierarchyhandle.md)
  A reference to a layer hierarchy that your app shares between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator)*