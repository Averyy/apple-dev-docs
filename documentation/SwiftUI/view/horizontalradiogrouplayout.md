# horizontalRadioGroupLayout()

**Framework**: SwiftUI  
**Kind**: method

Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func horizontalRadioGroupLayout() -> some View
```

#### Discussion

Use `horizontalRadioGroupLayout()` to configure the visual layout of radio buttons in a [`Picker`](picker.md) so that the radio buttons are arranged horizontally in the view.

The example below shows two [`Picker`](picker.md) controls configured as radio button groups; the first group shows the default vertical layout; the second group shows the effect of `horizontalRadioGroupLayout()` which renders the radio buttons horizontally.

```swift
struct HorizontalRadioGroupLayout: View {
    @State private var selected = 1
    var body: some View {
        VStack(spacing: 20) {
            Picker(selection: $selected, label: Text("Favorite Color")) {
                Text("Red").tag(1)
                Text("Green").tag(2)
                Text("Blue").tag(3)
                Text("Other").tag(4)
            }
            .pickerStyle(.radioGroup)

            Picker(selection: $selected, label: Text("Favorite Color")) {
                Text("Red").tag(1)
                Text("Green").tag(2)
                Text("Blue").tag(3)
                Text("Other").tag(4)
            }
            .pickerStyle(.radioGroup)
            .horizontalRadioGroupLayout()
        }
        .padding(20)
        .border(Color.gray)
    }
}
```

![A screenshot showing radio button groups laid out horizontally and](https://docs-assets.developer.apple.com/published/8f2854f2770dea6cb22a722e3aac8095/SwiftUI-view-horizontalRadioGroupLayout%402x.png)

## See Also

- [struct Picker](picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](view/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](view/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [struct PaletteSelectionEffect](paletteselectioneffect.md)
  The selection effect to apply to a palette item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/horizontalradiogrouplayout())*