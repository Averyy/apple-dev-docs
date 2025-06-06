# commit()

**Framework**: Browserenginekit  
**Kind**: method

`commit` must be called on  instance and it must be the last call to each instance. note that it does not commit `CATransaction`s but rather commits the coordination of transactions in the render server. note that coordinators should have as constrained a lifespan as possible and will timeout if held open too long.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func commit()
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)

#### Discussion

Notifies the render server to coordinate transactions for the added views and layer hierarchies.

#### Overview

You need to add all relevant views and layer hierarchies to the transaction coordinator, share the coordinator between processes, and make all necessary transactions before you call this method. When you call `commit()`, you can no longer use the transaction coordinator.

You need to call `commit()` as the last action on the transaction coordinator in all processes that use the same transaction coordinator.

> **Note**:  Committing a transaction coordinator synchronizes changes committed in [`CATransaction`](https://developer.apple.com/documentation/QuartzCore/CATransaction) objects that affect the added views and layer hierarchies, it doesn’t commit the transactions. You call [`commit()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/commit()) on each relevant transaction.

## See Also

- [func add(LayerHierarchyHostingView)](layerhierarchyhostingtransactioncoordinator/add(_:)-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func add(LayerHierarchy)](layerhierarchyhostingtransactioncoordinator/add(_:)-i66q.md)
  a signal to coordinate transactions involving `layerHierarchy` from now until `commit` is called


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/commit())*