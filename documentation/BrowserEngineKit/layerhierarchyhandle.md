# LayerHierarchyHandle

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A reference to a layer hierarchy that your app shares between processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class LayerHierarchyHandle
```

```objc
@interface BELayerHierarchyHandle : NSObject
```

## Mentions

- [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md)

## Overview

By sharing a reference, or *handle*, to your app’s layer hierarchy between processes, you can coordinate layer updates across multiple processes. Get a handle from a [`LayerHierarchy`](./layerhierarchy.md) object, then share it with another process using one of the serialization methods.

Use [`createXPCRepresentation()`](./layerhierarchyhandle/createxpcrepresentation%28%29.md) and [`init(xpcRepresentation:)`](./layerhierarchyhandle/init%28xpcrepresentation%29.md) to share layer handles across your app’s processes. Apps with existing Mach-based interprocess communication implementations can use [`encode(_:)`](./layerhierarchyhandle/encode%28_%29.md) and [`init(port:data:)`](./layerhierarchyhandle/init%28port,data%29.md) methods to share layer handles.

For more information, see [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md).

## Topics

### Sharing a layer hierarchy handle using XPC
- [func createXPCRepresentation() -> xpc_object_t](./layerhierarchyhandle/createxpcrepresentation%28%29.md)
  Creates an object representing this handle that you send to another process in an XPC message.
- [init(xpcRepresentation: xpc_object_t?) throws](./layerhierarchyhandle/init%28xpcrepresentation%29.md)
  Creates a handle from a representation received in an XPC message.
### Sharing a layer hierarchy handle using Mach
- [func encode((mach_port_t, Data) -> Void)](./layerhierarchyhandle/encode%28_%29.md)
  Serializes the hierarchy handle into a Mach port reference and accompanying data.
- [init(port: mach_port_t, data: Data) throws](./layerhierarchyhandle/init%28port,data%29.md)
  Creates a layer hierarchy handle using a Mach port reference and serialized data.
### Creating a layer hierarchy handle
- [init?(coder: NSCoder)](./layerhierarchyhandle/init%28coder%29.md)
  Creates a handle from an encoded representation.

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
- [class LayerHierarchyHostingTransactionCoordinator](./layerhierarchyhostingtransactioncoordinator.md)
  A class that synchronizes updates to views and layers in different processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle)*