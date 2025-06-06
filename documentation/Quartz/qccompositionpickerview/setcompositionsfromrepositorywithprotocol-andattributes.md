# setCompositionsFromRepositoryWithProtocol(_:andAttributes:)

**Framework**: Quartz  
**Kind**: method

Sets the  compositions in the composition picker view  to those that match the specified criteria.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setCompositionsFromRepositoryWithProtocol(_ protocol: String!, andAttributes attributes: [AnyHashable : Any]! = [:])
```

## Parameters

- `protocol`: The protocols that you want compositions shown in the picker view to conform to. You can pass any of these protocols: QCCompositionProtocolAnimation, QCCompositionProtocolImageProducer, QCCompositionProtocolImageFilter, QCCompositionProtocolImageCompositor, and QCCompositionProtocolScreenSaverRSS.
- `attributes`: A dictionary that contains the attributes, and their associated values, that you want compositions in the picker view to match. For example, you can pass: QCCompositionAttributeNameKey, QCCompositionAttributeDescriptionKey, QCCompositionAttributeCopyrightKey, and QCCompositionAttributeBuiltInKey. Pass   if you don’t want to filter based on the attributes.

## See Also

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
- [func selectedComposition() -> QCComposition!](qccompositionpickerview/selectedcomposition.md)
  Returns the composition that is currently selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setcompositionsfromrepositorywithprotocol(_:andattributes:))*