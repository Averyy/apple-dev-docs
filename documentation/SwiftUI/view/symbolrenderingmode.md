# symbolRenderingMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the rendering mode for symbol images within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> some View
```

#### Return Value

A view that uses the rendering mode you supply.

## Parameters

- `mode`: The symbol rendering mode to use.

## See Also

- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [struct SymbolRenderingMode](symbolrenderingmode.md)
  A symbol rendering mode.
- [struct SymbolColorRenderingMode](symbolcolorrenderingmode.md)
  A method of filling a layer in a symbol image.
- [struct SymbolVariableValueMode](symbolvariablevaluemode.md)
  A method of rendering the variable value of a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/symbolrenderingmode(_:))*