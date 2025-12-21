# loadComposition(fromFile:)

**Framework**: Quartz  
**Kind**: method

Loads the composition file located at the specified path.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func loadComposition(fromFile path: String!) -> Bool
```

#### Return Value

If unsuccessful, returns [`false`](https://developer.apple.com/documentation/Swift/false); any composition that’s already loaded in the view remains loaded.

## Parameters

- `path`: A string that specifies the location of a Quartz Composer composition file.

## See Also

- [func load(QCComposition!) -> Bool](qcview/load(_:).md)
  Loads a [`QCComposition`](qccomposition.md) object into the view.
- [func loadedComposition() -> QCComposition!](qcview/loadedcomposition.md)
  Returns the composition loaded in the view.
- [func unloadComposition()](qcview/unloadcomposition.md)
  Unloads the composition from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/loadcomposition(fromfile:))*