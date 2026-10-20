# load(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Loads a [`QCComposition`](../qccomposition.md) object into the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func load(_ composition: QCComposition!) -> Bool
```

```objc
- (BOOL) loadComposition:(QCComposition *) composition;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise [`false`](../../Swift/false.md). If unsuccessful, any composition that’s already loaded in the view remains loaded.

## Parameters

- `composition`: The [`QCComposition`](../qccomposition.md) object to load.

## See Also

### Loading a Composition
- [func loadComposition(fromFile: String!) -> Bool](./loadcomposition%28fromfile%29.md)
  Loads the composition file located at the specified path.
- [func loadedComposition() -> QCComposition!](./loadedcomposition%28%29.md)
  Returns the composition loaded in the view.
- [func unloadComposition()](./unloadcomposition%28%29.md)
  Unloads the composition from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/load(_:))*