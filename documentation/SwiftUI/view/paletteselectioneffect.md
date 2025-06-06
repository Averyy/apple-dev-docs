# paletteSelectionEffect(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the selection effect to apply to a palette item.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func paletteSelectionEffect(_ effect: PaletteSelectionEffect) -> some View
```

#### Discussion

[`automatic`](paletteselectioneffect/automatic.md) applies the system’s default appearance when selected. When using un-tinted SF Symbols or template images, the current tint color is applied to the selected items’ image. If the provided SF Symbols have custom tints, a stroke is drawn around selected items.

If you wish to provide a specific image (or SF Symbol) to indicate selection, use [`custom`](paletteselectioneffect/custom.md) to forgo the system’s default selection appearance allowing the provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system selection behavior:

```swift
Menu {
    Picker("Palettes", selection: $selection) {
        ForEach(palettes) { palette in
            Label(palette.title, image: selection == palette ?
                  "selected-palette" : "palette")
            .tint(palette.tint)
            .tag(palette)
        }
    }
    .pickerStyle(.palette)
    .paletteSelectionEffect(.custom)
} label: {
    ...
}
```

If a specific SF Symbol variant is preferable instead, use [`symbolVariant(_:)`](paletteselectioneffect/symbolvariant(_:).md).

```swift
Menu {
    ControlGroup {
        ForEach(ColorTags.allCases) { colorTag in
            Toggle(isOn: $selectedColorTags[colorTag]) {
                Label(colorTag.name, systemImage: "circle")
            }
            .tint(colorTag.color)
        }
    }
    .controlGroupStyle(.palette)
    .paletteSelectionEffect(.symbolVariant(.fill))
}
```

## Parameters

- `effect`: The type of effect to apply when a palette item is selected.

## See Also

- [struct Picker](picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func horizontalRadioGroupLayout() -> some View](view/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](view/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [struct PaletteSelectionEffect](paletteselectioneffect.md)
  The selection effect to apply to a palette item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/paletteselectioneffect(_:))*