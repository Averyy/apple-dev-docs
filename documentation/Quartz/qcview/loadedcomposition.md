# loadedComposition()

**Framework**: Quartz  
**Kind**: method

Returns the composition loaded in the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func loadedComposition() -> QCComposition!
```

#### Return Value

The composition loaded in the view; otherwise `nil`.

## See Also

- [func loadComposition(fromFile: String!) -> Bool](qcview/loadcomposition(fromfile:).md)
  Loads the composition file located at the specified path.
- [func load(QCComposition!) -> Bool](qcview/load(_:).md)
  Loads a [`QCComposition`](qccomposition.md) object into the view.
- [func unloadComposition()](qcview/unloadcomposition.md)
  Unloads the composition from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/loadedcomposition())*