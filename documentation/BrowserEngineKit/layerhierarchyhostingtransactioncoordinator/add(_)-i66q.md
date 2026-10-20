# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func add(_ layerHierarchy: LayerHierarchy)
```

```objc
- (void) addLayerHierarchy:(BELayerHierarchy *) layerHierarchy;
```

#### Discussion

The transaction coordinator coordinates any transactions involving layers in the `layerHierarchy` until you call [`commit()`](./commit%28%29.md).

## Parameters

- `layerHierarchy`: The object to coordinate transactions for.

## See Also

### Synchronizing transactions
- [func add(LayerHierarchyHostingView)](./add%28_%29-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func commit()](./commit%28%29.md)
  Notifies the render server to coordinate transactions for the added views and layer hierarchies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/add(_:)-i66q)*