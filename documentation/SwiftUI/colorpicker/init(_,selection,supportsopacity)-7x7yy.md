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
init<S>(_ title: S, selection: Binding<CGColor>, supportsOpacity: Bool = true) where S : StringProtocol
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
init<S>(_ title: S, selection: Binding<Color>, supportsOpacity: Bool = true) where S : StringProtocol
```

## Parameters

- `title`: The title displayed by the color picker.
- `selection`: A [`Binding`](../binding.md) to the variable containing a `CGColor`.
- `supportsOpacity`: A Boolean value that indicates whether the color picker allows adjustments to the selected color’s opacity; the default is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:)-7x7yy)*