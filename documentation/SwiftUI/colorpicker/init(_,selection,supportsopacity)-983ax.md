# init(_:selection:supportsOpacity:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color picker with a text label generated from a title string key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool = true)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<CGColor>, supportsOpacity: Bool = true)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Color>, supportsOpacity: Bool = true)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool = true)
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<CGColor>, supportsOpacity: Bool = true) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Color>, supportsOpacity: Bool = true) where S : StringProtocol
```

## Discussion

Use [`ColorPicker`](../colorpicker.md) to create a color well that your app uses to allow the selection of a [`Color`](../color.md). The example below creates a color well using a [`Binding`](../binding.md) to a property stored in a settings object and title you provide:

```swift
final class Settings: ObservableObject {
    @Published var alignmentGuideColor =
        Color(.sRGB, red: 0.98, green: 0.9, blue: 0.2)
}

struct FormattingControls: View {
    @State private var settings = Settings()

    var body: some View {
        VStack {
            // Other formatting controls.
            ColorPicker("Alignment Guides",
                selection: $settings.alignmentGuideColor
            )
        }
    }
}
```

## Parameters

- `titleKey`: The key for the localized title of the picker.
- `selection`: A [`Binding`](../binding.md) to the variable that displays the selected [`Color`](../color.md).
- `supportsOpacity`: A Boolean value that indicates whether the color picker allows adjustments to the selected color’s opacity; the default is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:)-983ax)*