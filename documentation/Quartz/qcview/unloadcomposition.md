# unloadComposition()

**Framework**: Quartz  
**Kind**: method

Unloads the composition from the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func unloadComposition()
```

#### Discussion

If necessary, this method calls [`stopRendering()`](qcview/stoprendering().md)  prior to unloading the composition.

## See Also

- [func loadComposition(fromFile: String!) -> Bool](qcview/loadcomposition(fromfile:).md)
  Loads the composition file located at the specified path.
- [func load(QCComposition!) -> Bool](qcview/load(_:).md)
  Loads a [`QCComposition`](qccomposition.md) object into the view.
- [func loadedComposition() -> QCComposition!](qcview/loadedcomposition.md)
  Returns the composition loaded in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/unloadcomposition())*