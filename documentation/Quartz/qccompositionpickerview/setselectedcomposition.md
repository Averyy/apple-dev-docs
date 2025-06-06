# setSelectedComposition(_:)

**Framework**: Quartz  
**Kind**: method

Sets a composition as selected in the composition picker view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setSelectedComposition(_ composition: QCComposition!)
```

## Parameters

- `composition`: The composition to select. Pass   if you don’t want to select a composition. The behavior is undefined if you pass a composition that is not in the list of compositions that are currently in the composition picker view.

## See Also

- [func setCompositionsFromRepositoryWithProtocol(String!, andAttributes: [AnyHashable : Any]!)](qccompositionpickerview/setcompositionsfromrepositorywithprotocol(_:andattributes:).md)
  Sets the  compositions in the composition picker view  to those that match the specified criteria.
- [func compositions() -> [Any]!](qccompositionpickerview/compositions.md)
  Returns the list of compositions that are currently in the composition picker view.
- [func setAllowsEmptySelection(Bool)](qccompositionpickerview/setallowsemptyselection(_:).md)
  Sets whether to allow an empty selection in the composition picker view.
- [func allowsEmptySelection() -> Bool](qccompositionpickerview/allowsemptyselection.md)
  Retrieves the empty-selection state of the composition picker view.
- [func setCompositionAspectRatio(NSSize)](qccompositionpickerview/setcompositionaspectratio(_:).md)
  Sets  the aspect ratio used to display compositions in the composition picker view.
- [func compositionAspectRatio() -> NSSize](qccompositionpickerview/compositionaspectratio.md)
  Retrieves the aspect ratio used to display compositions in the composition picker  view.
- [func selectedComposition() -> QCComposition!](qccompositionpickerview/selectedcomposition.md)
  Returns the composition that is currently selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setselectedcomposition(_:))*