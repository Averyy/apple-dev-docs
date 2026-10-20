# setCompositionsFromRepositoryWithProtocol(_:andAttributes:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the  compositions in the composition picker view  to those that match the specified criteria.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setCompositionsFromRepositoryWithProtocol(_ protocol: String!, andAttributes attributes: [AnyHashable : Any]! = [:])
```

```objc
- (void) setCompositionsFromRepositoryWithProtocol:(NSString *) protocol andAttributes:(NSDictionary *) attributes;
```

## Parameters

- `protocol`: The protocols that you want compositions shown in the picker view to conform to. You can pass any of these protocols: QCCompositionProtocolAnimation, QCCompositionProtocolImageProducer, QCCompositionProtocolImageFilter, QCCompositionProtocolImageCompositor, and QCCompositionProtocolScreenSaverRSS.
- `attributes`: A dictionary that contains the attributes, and their associated values, that you want compositions in the picker view to match. For example, you can pass: QCCompositionAttributeNameKey, QCCompositionAttributeDescriptionKey, QCCompositionAttributeCopyrightKey, and QCCompositionAttributeBuiltInKey. Pass `nil` if you don’t want to filter based on the attributes.

## See Also

### Managing the Composition Picker View
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
- [func setSelectedComposition(QCComposition!)](./setselectedcomposition%28_%29.md)
  Sets a composition as selected in the composition picker view.
- [func selectedComposition() -> QCComposition!](./selectedcomposition%28%29.md)
  Returns the composition that is currently selected in the composition picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setcompositionsfromrepositorywithprotocol(_:andattributes:))*