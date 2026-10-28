# unloadComposition()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Unloads the composition from the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func unloadComposition()
```

```objc
- (void) unloadComposition;
```

## Discussion

If necessary, this method calls [`stopRendering()`](./stoprendering%28%29.md)  prior to unloading the composition.

## See Also

### Loading a Composition
- [func loadComposition(fromFile: String!) -> Bool](./loadcomposition%28fromfile%29.md)
  Loads the composition file located at the specified path.
- [func load(QCComposition!) -> Bool](./load%28_%29.md)
  Loads a [`QCComposition`](../qccomposition.md) object into the view.
- [func loadedComposition() -> QCComposition!](./loadedcomposition%28%29.md)
  Returns the composition loaded in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/unloadcomposition())*