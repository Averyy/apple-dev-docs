# SymbolVariableValueMode

**Framework**: SwiftUI  
**Kind**: struct

A method of rendering the variable value of a symbol image.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct SymbolVariableValueMode
```

## Topics

### Type Properties
- [static let color: SymbolVariableValueMode](symbolvariablevaluemode/color.md)
  The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [static let draw: SymbolVariableValueMode](symbolvariablevaluemode/draw.md)
  The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.

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
- [struct SymbolColorRenderingMode](symbolcolorrenderingmode.md)
  A method of filling a layer in a symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariablevaluemode)*