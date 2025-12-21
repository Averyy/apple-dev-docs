# SymbolColorRenderingMode

**Framework**: SwiftUI  
**Kind**: struct

A method of filling a layer in a symbol image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SymbolColorRenderingMode
```

## Topics

### Type Properties
- [static let flat: SymbolColorRenderingMode](symbolcolorrenderingmode/flat.md)
  The symbol image layer should be filled with a solid color.
- [static let gradient: SymbolColorRenderingMode](symbolcolorrenderingmode/gradient.md)
  The symbol image layer should be filled with an axial gradient.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](view/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [struct SymbolRenderingMode](symbolrenderingmode.md)
  A symbol rendering mode.
- [struct SymbolVariableValueMode](symbolvariablevaluemode.md)
  A method of rendering the variable value of a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolcolorrenderingmode)*