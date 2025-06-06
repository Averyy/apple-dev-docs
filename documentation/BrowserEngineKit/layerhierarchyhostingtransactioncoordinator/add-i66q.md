# add(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

a signal to coordinate transactions involving `layerHierarchy` from now until `commit` is called

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
func add(_ layerHierarchy: LayerHierarchy)
```

#### Discussion

Notifies the transaction coordinator to start coordinating transactions for the given layer hierarchy.

#### Overview

The transaction coordinator coordinates any transactions involving layers in the `layerHierarchy` until you call [`commit()`](layerhierarchyhostingtransactioncoordinator/commit().md).

## Parameters

- `layerHierarchy`: The object to coordinate transactions for.

## See Also

- [func add(LayerHierarchyHostingView)](layerhierarchyhostingtransactioncoordinator/add(_:)-7day0.md)
  Notifies the transaction coordinator to start coordinating transactions for the given view.
- [func commit()](layerhierarchyhostingtransactioncoordinator/commit.md)
  `commit` must be called on  instance and it must be the last call to each instance. note that it does not commit `CATransaction`s but rather commits the coordination of transactions in the render server. note that coordinators should have as constrained a lifespan as possible and will timeout if held open too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/add(_:)-i66q)*