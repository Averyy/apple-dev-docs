# load(_:)

**Framework**: Quartz  
**Kind**: method

Loads a [`QCComposition`](qccomposition.md) object into the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func load(_ composition: QCComposition!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; otherwise [`false`](https://developer.apple.com/documentation/Swift/false). If unsuccessful, any composition that’s already loaded in the view remains loaded.

## Parameters

- `composition`: The   object to load.

## See Also

- [func loadComposition(fromFile: String!) -> Bool](qcview/loadcomposition(fromfile:).md)
  Loads the composition file located at the specified path.
- [func loadedComposition() -> QCComposition!](qcview/loadedcomposition.md)
  Returns the composition loaded in the view.
- [func unloadComposition()](qcview/unloadcomposition.md)
  Unloads the composition from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/load(_:))*