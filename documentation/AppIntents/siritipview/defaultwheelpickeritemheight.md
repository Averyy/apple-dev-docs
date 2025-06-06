# defaultWheelPickerItemHeight(_:)

**Framework**: App Intents  
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

## Parameters

- `height`: The height for the picker items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/defaultwheelpickeritemheight(_:))*