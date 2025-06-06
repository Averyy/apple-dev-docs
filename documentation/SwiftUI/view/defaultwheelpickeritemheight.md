# defaultWheelPickerItemHeight(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the default wheel-style picker item height.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
func defaultWheelPickerItemHeight(_ height: CGFloat) -> some View
```

#### Discussion

Use `defaultWheelPickerItemHeight(_:)` when you need to change the default item height in a picker control. In this example, the view sets the default height for picker elements to 30 points.

```swift
struct DefaultWheelPickerItemHeight: View {
    @State private var selected = 1
    var body: some View {
        VStack(spacing: 20) {
            Picker(selection: $selected, label: Text("Favorite Color")) {
                Text("Red").tag(1)
                Text("Green").tag(2)
                Text("Blue").tag(3)
                Text("Other").tag(4)
            }
        }
        .defaultWheelPickerItemHeight(30)
    }
}
```

![A screenshot showing the effect changing the height of picker wheel](https://docs-assets.developer.apple.com/published/0bee1da82c48cdfec06989ba7daeade4/SwiftUI-View-defaultWheelPickerItemHeight%402x.png)

## Parameters

- `height`: The height for the picker items.

## See Also

- [struct Picker](picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func horizontalRadioGroupLayout() -> some View](view/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](view/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [struct PaletteSelectionEffect](paletteselectioneffect.md)
  The selection effect to apply to a palette item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultwheelpickeritemheight(_:))*