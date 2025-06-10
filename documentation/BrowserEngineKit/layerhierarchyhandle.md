# LayerHierarchyHandle

**Framework**: BrowserEngineKit  
**Kind**: class

A reference to a layer hierarchy that you share between processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class LayerHierarchyHandle
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

## Topics

### Interprocess communication
- [init?(coder: NSCoder)](layerhierarchyhandle/init(coder:).md)
  Creates a handle from an encoded representation.
- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhandle/init(xpcrepresentation:).md)
  Creates a handle from a representation received in an XPC message.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhandle/createxpcrepresentation.md)
  Creates an object representing this handle that you send to another process in an XPC message.
### Initializers
- [init(port: mach_port_t, data: Data) throws](layerhierarchyhandle/init(port:data:).md)
  takes ownership of the port right (even if it returns nil).
### Instance Methods
- [func encode((mach_port_t, Data) -> Void)](layerhierarchyhandle/encode(_:).md)
  passes a copy of the send right or `MACH_PORT_NULL` if inert. the receiver is responsible for disposing of `copiedPort`. the port and data should be consumed together and  once by `init(port:data:)`.

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
  Synchronizes updates to views and layers in different processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle)*