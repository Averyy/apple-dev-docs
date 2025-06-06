# pickerStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for pickers within this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func pickerStyle<S>(_ style: S) -> some View where S : PickerStyle
```

## See Also

- [struct Picker](picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func horizontalRadioGroupLayout() -> some View](view/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](view/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](view/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [struct PaletteSelectionEffect](paletteselectioneffect.md)
  The selection effect to apply to a palette item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/pickerstyle(_:))*