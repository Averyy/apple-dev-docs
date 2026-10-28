# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Notifies the transaction coordinator to start coordinating transactions for the given view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func add(_ hostingView: LayerHierarchyHostingView)
```

```objc
- (void) addLayerHierarchyHostingView:(BELayerHierarchyHostingView *) hostingView;
```

## Discussion

The transaction coordinator coordinates any transactions involving `hostingView` until you call [`commit()`](./commit%28%29.md).

## Parameters

- `hostingView`: The view to coordinate transactions for.

## See Also

### Synchronizing transactions
- [func add(LayerHierarchy)](./add%28_%29-i66q.md)
  Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.
- [func commit()](./commit%28%29.md)
  Notifies the render server to coordinate transactions for the added views and layer hierarchies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/add(_:)-7day0)*