# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func add(_ layerHierarchy: LayerHierarchy)
```

#### Discussion

The transaction coordinator coordinates any transactions involving layers in the `layerHierarchy` until you call [`commit()`](layerhierarchyhostingtransactioncoordinator/commit().md).

## Parameters

- `layerHierarchy`: The object to coordinate transactions for.

## See Also

- [func add(LayerHierarchyHostingView)](layerhierarchyhostingtransactioncoordinator/add(_:)-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func commit()](layerhierarchyhostingtransactioncoordinator/commit.md)
  Notifies the render server to coordinate transactions for the added views and layer hierarchies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/add(_:)-i66q)*