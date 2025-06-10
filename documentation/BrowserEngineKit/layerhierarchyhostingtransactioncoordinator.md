# LayerHierarchyHostingTransactionCoordinator

**Framework**: BrowserEngineKit  
**Kind**: class

Synchronizes updates to views and layers in different processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class LayerHierarchyHostingTransactionCoordinator
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

## Topics

### Creating a transaction coordinator
- [init() throws](layerhierarchyhostingtransactioncoordinator/init.md)
  may fail if a connection to the render server cannot be established
### Interprocess communication
- [init?(coder: NSCoder)](layerhierarchyhostingtransactioncoordinator/init(coder:).md)
  Creates a transaction coordinator from an encoded representation.
- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhostingtransactioncoordinator/init(xpcrepresentation:).md)
  Creates a transaction coordinator from an XPC object.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhostingtransactioncoordinator/createxpcrepresentation.md)
  Creates a representation of the transaction coordinator you send to another process.
### Synchronize transactions
- [func add(LayerHierarchyHostingView)](layerhierarchyhostingtransactioncoordinator/add(_:)-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func add(LayerHierarchy)](layerhierarchyhostingtransactioncoordinator/add(_:)-i66q.md)
  a signal to coordinate transactions involving `layerHierarchy` from now until `commit` is called
- [func commit()](layerhierarchyhostingtransactioncoordinator/commit.md)
  `commit` must be called on  instance and it must be the last call to each instance. note that it does not commit `CATransaction`s but rather commits the coordination of transactions in the render server. note that coordinators should have as constrained a lifespan as possible and will timeout if held open too long.
### Initializers
- [init(port: mach_port_t, data: Data) throws](layerhierarchyhostingtransactioncoordinator/init(port:data:).md)
  takes ownership of the port right (even if it returns nil).
### Instance Methods
- [func encode((mach_port_t, Data) -> Void)](layerhierarchyhostingtransactioncoordinator/encode(_:).md)
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
- [class LayerHierarchyHandle](layerhierarchyhandle.md)
  A reference to a layer hierarchy that you share between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator)*