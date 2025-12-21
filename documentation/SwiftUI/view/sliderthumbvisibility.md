# sliderThumbVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the thumb visibility for `Slider`s within this view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func sliderThumbVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

Use this modifier to override the default slider thumb visibility. For example, the code below creates a `Slider` without an indicator:

```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    VStack {
        Slider(
            value: $speed,
            in: 0...100,
            onEditingChanged: { editing in
                isEditing = editing
            }
        )
        .sliderThumbVisibility(.hidden)

        Text("\(speed)")
            .foregroundColor(isEditing ? .red : .blue)
    }
}
```

Note: On watchOS, the slider thumb is always visible.

## Parameters

- `visibility`: The slider thumb visibility to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sliderthumbvisibility(_:))*