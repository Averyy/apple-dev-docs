# LayerHierarchy

**Framework**: BrowserEngineKit  
**Kind**: class

An object that holds a reference to layers rendered in another process’s view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class LayerHierarchy
```

## Mentions

- [Propagating view visibility information to extension processes](propagating-view-visibility-information-to-browser-extensions.md)
- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

#### Overview

In your browser’s rendering extension, create a `LayerHierarchy` and set its [`layer`](layerhierarchy/layer.md) to a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) that renders content to host in a view in the browser app. Get the layer hierarchy’s [`handle`](layerhierarchy/handle.md), and send it to the browser app, where you add the handle to a [`LayerHierarchyHostingView`](layerhierarchyhostingview.md).

Use [`LayerHierarchyHostingTransactionCoordinator`](layerhierarchyhostingtransactioncoordinator.md) to synchronize updates in the view and the layer. For more information, see [`Hosting browser view layers in the rendering extension`](hosting-browser-view-layers-in-the-rendering-extension.md).

## Topics

### Creating and invalidating a layer hierarchy
- [init() throws](layerhierarchy/init.md)
  Initializes a layer hierarchy.
- [func invalidate()](layerhierarchy/invalidate.md)
  Invalidates a layer hierarchy.
### Setting the layer
- [var layer: CALayer?](layerhierarchy/layer.md)
  The layer represented by this layer hierarchy.
### Getting a handle
- [var handle: LayerHierarchyHandle](layerhierarchy/handle.md)
  A reference to the layer hierarchy that you add to the hosting view.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchyHostingView](layerhierarchyhostingview.md)
  A view that hosts a layer hierarchy you manage in another process.
- [class LayerHierarchyHostingTransactionCoordinator](layerhierarchyhostingtransactioncoordinator.md)
  Synchronizes updates to views and layers in different processes.
- [class LayerHierarchyHandle](layerhierarchyhandle.md)
  A reference to a layer hierarchy that you share between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchy)*