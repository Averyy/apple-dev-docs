# init(_:selection:supportsOpacity:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a color picker with a text label generated from a title string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Color>, supportsOpacity: Bool = true) where S : StringProtocol
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
init(_ titleKey: LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool = true)
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<CGColor>, supportsOpacity: Bool = true) where S : StringProtocol
```

## Discussion

Use [`ColorPicker`](../colorpicker.md) to create a color well that your app uses to allow the selection of a [`Color`](../color.md). The example below creates a color well using a [`Binding`](../binding.md) and title you provide:

```swift
func showColorPicker(_ title: String, color: Binding<Color>) {
    ColorPicker(title, selection: color)
}
```

## Parameters

- `title`: The title displayed by the color picker.
- `selection`: A [`Binding`](../binding.md) to the variable containing a [`Color`](../color.md).
- `supportsOpacity`: A Boolean value that indicates whether the color picker allows adjustments to the selected color’s opacity; the default is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:)-7cued)*