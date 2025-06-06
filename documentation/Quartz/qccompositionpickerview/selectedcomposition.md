# selectedComposition()

**Framework**: Quartz  
**Kind**: method

Returns the composition that is currently selected in the composition picker view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func selectedComposition() -> QCComposition!
```

#### Return Value

A `QCComposition` object, or `nil` if a composition is not selected.

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
- [func setSelectedComposition(QCComposition!)](qccompositionpickerview/setselectedcomposition(_:).md)
  Sets a composition as selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/selectedcomposition())*