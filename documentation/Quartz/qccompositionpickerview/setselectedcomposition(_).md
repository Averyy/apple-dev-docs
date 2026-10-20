# setSelectedComposition(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets a composition as selected in the composition picker view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setSelectedComposition(_ composition: QCComposition!)
```

```objc
- (void) setSelectedComposition:(QCComposition *) composition;
```

## Parameters

- `composition`: The composition to select. Pass `nil` if you don’t want to select a composition. The behavior is undefined if you pass a composition that is not in the list of compositions that are currently in the composition picker view.

## See Also

### Managing the Composition Picker View
- [func setCompositionsFromRepositoryWithProtocol(String!, andAttributes: [AnyHashable : Any]!)](./setcompositionsfromrepositorywithprotocol%28_,andattributes%29.md)
  Sets the  compositions in the composition picker view  to those that match the specified criteria.
- [func compositions() -> [Any]!](./compositions%28%29.md)
  Returns the list of compositions that are currently in the composition picker view.
- [func setAllowsEmptySelection(Bool)](./setallowsemptyselection%28_%29.md)
  Sets whether to allow an empty selection in the composition picker view.
- [func allowsEmptySelection() -> Bool](./allowsemptyselection%28%29.md)
  Retrieves the empty-selection state of the composition picker view.
- [func setCompositionAspectRatio(NSSize)](./setcompositionaspectratio%28_%29.md)
  Sets  the aspect ratio used to display compositions in the composition picker view.
- [func compositionAspectRatio() -> NSSize](./compositionaspectratio%28%29.md)
  Retrieves the aspect ratio used to display compositions in the composition picker  view.
- [func selectedComposition() -> QCComposition!](./selectedcomposition%28%29.md)
  Returns the composition that is currently selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setselectedcomposition(_:))*