# commit()

**Framework**: BrowserEngineKit  
**Kind**: method

Notifies the render server to coordinate transactions for the added views and layer hierarchies.

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

In all processes that share a transaction coordinator instance, call this method as the last interaction with the instance.

Before calling this method:

- Add the relevant views and layer hierarchies to the transaction coordinator.
- Share the coordinator between processes.
- Perform the necessary transactions.

Use the instance only once; after you call this method, discard the instance.

> **Note**: This method synchronizes changes committed in [`CATransaction`](https://developer.apple.com/documentation/quartzcore/catransaction) objects that affect the added views and layer hierarchies; it doesn’t commit the transactions. Call [`commit()`](https://developer.apple.com/documentation/quartzcore/catransaction/commit()) on each relevant transaction.

## See Also

- [func add(LayerHierarchyHostingView)](layerhierarchyhostingtransactioncoordinator/add(_:)-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func add(LayerHierarchy)](layerhierarchyhostingtransactioncoordinator/add(_:)-i66q.md)
  Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/commit())*