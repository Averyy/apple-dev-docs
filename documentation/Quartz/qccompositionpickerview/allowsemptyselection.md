# allowsEmptySelection()

**Framework**: Quartz  
**Kind**: method

Retrieves the empty-selection state of the composition picker view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func allowsEmptySelection() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an empty selection is allowed [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [func setCompositionsFromRepositoryWithProtocol(String!, andAttributes: [AnyHashable : Any]!)](qccompositionpickerview/setcompositionsfromrepositorywithprotocol(_:andattributes:).md)
  Sets the  compositions in the composition picker view  to those that match the specified criteria.
- [func compositions() -> [Any]!](qccompositionpickerview/compositions.md)
  Returns the list of compositions that are currently in the composition picker view.
- [func setAllowsEmptySelection(Bool)](qccompositionpickerview/setallowsemptyselection(_:).md)
  Sets whether to allow an empty selection in the composition picker view.
- [func setCompositionAspectRatio(NSSize)](qccompositionpickerview/setcompositionaspectratio(_:).md)
  Sets  the aspect ratio used to display compositions in the composition picker view.
- [func compositionAspectRatio() -> NSSize](qccompositionpickerview/compositionaspectratio.md)
  Retrieves the aspect ratio used to display compositions in the composition picker  view.
- [func setSelectedComposition(QCComposition!)](qccompositionpickerview/setselectedcomposition(_:).md)
  Sets a composition as selected in the composition picker view.
- [func selectedComposition() -> QCComposition!](qccompositionpickerview/selectedcomposition.md)
  Returns the composition that is currently selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/allowsemptyselection())*