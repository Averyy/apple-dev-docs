# loadComposition(fromFile:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Loads the composition file located at the specified path.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func loadComposition(fromFile path: String!) -> Bool
```

```objc
- (BOOL) loadCompositionFromFile:(NSString *) path;
```

## Return Value

If unsuccessful, returns [`false`](../../Swift/false.md); any composition that’s already loaded in the view remains loaded.

## Parameters

- `path`: A string that specifies the location of a Quartz Composer composition file.

## See Also

### Loading a Composition
- [func load(QCComposition!) -> Bool](./load%28_%29.md)
  Loads a [`QCComposition`](../qccomposition.md) object into the view.
- [func loadedComposition() -> QCComposition!](./loadedcomposition%28%29.md)
  Returns the composition loaded in the view.
- [func unloadComposition()](./unloadcomposition%28%29.md)
  Unloads the composition from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/loadcomposition(fromfile:))*