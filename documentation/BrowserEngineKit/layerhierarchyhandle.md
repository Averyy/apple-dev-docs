# LayerHierarchyHandle

**Framework**: BrowserEngineKit  
**Kind**: class

A reference to a layer hierarchy that your app shares between processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class LayerHierarchyHandle
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

#### Overview

By sharing a reference, or *handle*, to your app’s layer hierarchy between processes, you can coordinate layer updates across multiple processes. Get a handle from a [`LayerHierarchy`](layerhierarchy.md) object, then share it with another process using one of the serialization methods.

Use [`createXPCRepresentation()`](layerhierarchyhandle/createxpcrepresentation().md) and [`init(xpcRepresentation:)`](layerhierarchyhandle/init(xpcrepresentation:).md) to share layer handles across your app’s processes. Apps with existing Mach-based interprocess communication implementations can use [`encode(_:)`](layerhierarchyhandle/encode(_:).md) and [`init(port:data:)`](layerhierarchyhandle/init(port:data:).md) methods to share layer handles.

For more information, see [`Hosting browser view layers in the rendering extension`](hosting-browser-view-layers-in-the-rendering-extension.md).

## Topics

### Sharing a layer hierarchy handle using XPC
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhandle/createxpcrepresentation.md)
  Creates an object representing this handle that you send to another process in an XPC message.
- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhandle/init(xpcrepresentation:).md)
  Creates a handle from a representation received in an XPC message.
### Sharing a layer hierarchy handle using Mach
- [func encode((mach_port_t, Data) -> Void)](layerhierarchyhandle/encode(_:).md)
  Serializes the hierarchy handle into a Mach port reference and accompanying data.
- [init(port: mach_port_t, data: Data) throws](layerhierarchyhandle/init(port:data:).md)
  Creates a layer hierarchy handle using a Mach port reference and serialized data.
### Creating a layer hierarchy handle
- [init?(coder: NSCoder)](layerhierarchyhandle/init(coder:).md)
  Creates a handle from an encoded representation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingView](layerhierarchyhostingview.md)
  A view that hosts a layer hierarchy you manage in another process.
- [class LayerHierarchyHostingTransactionCoordinator](layerhierarchyhostingtransactioncoordinator.md)
  A class that synchronizes updates to views and layers in different processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle)*