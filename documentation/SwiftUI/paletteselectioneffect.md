# PaletteSelectionEffect

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The selection effect to apply to a palette item.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct PaletteSelectionEffect
```

#### Overview

You can configure the selection effect of a palette item by using the [`paletteSelectionEffect(_:)`](./view/paletteselectioneffect%28_%29.md) view modifier.

## Topics

### Getting palette selection effects
- [static let automatic: PaletteSelectionEffect](./paletteselectioneffect/automatic.md)
  Applies the system’s default effect when selected.
- [static let custom: PaletteSelectionEffect](./paletteselectioneffect/custom.md)
  Does not apply any system effect when selected.
- [static func symbolVariant(SymbolVariants) -> PaletteSelectionEffect](./paletteselectioneffect/symbolvariant%28_%29.md)
  Applies the specified symbol variant when selected.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Choosing from a set of options
- [struct Picker](./picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func pickerStyle<S>(S) -> some View](./view/pickerstyle%28_%29.md)
  Sets the style for pickers within this view.
- [func horizontalRadioGroupLayout() -> some View](./view/horizontalradiogrouplayout%28%29.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](./view/defaultwheelpickeritemheight%28_%29.md)
  Sets the default wheel-style picker item height.
- [var defaultWheelPickerItemHeight: CGFloat](./environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](./view/paletteselectioneffect%28_%29.md)
  Specifies the selection effect to apply to a palette item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/paletteselectioneffect)*