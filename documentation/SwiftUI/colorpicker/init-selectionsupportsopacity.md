# init(_:selection:supportsOpacity:)

**Framework**: SwiftUI  
**Kind**: init

Creates a color picker with a text label generated from a title string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<CGColor>, supportsOpacity: Bool = true)
```

## Parameters

- `titleResource`: The localized title of the picker.
- `selection`: A [`Binding`](binding.md) to the variable that displays the selected `CGColor`.
- `supportsOpacity`: A Boolean value that indicates whether the color picker allows adjustments to the selected color’s opacity; the default is `true`.

## See Also

- [init(selection:supportsOpacity:label:)](colorpicker/init(selection:supportsopacity:label:).md)
  Creates an instance that selects a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:))*