# init(_:selection:supportsOpacity:)

**Framework**: SwiftUI  
**Kind**: init

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
init(_ titleKey: LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool = true)
```

## Parameters

- `titleKey`: The key for the localized title of the picker.
- `selection`: A   to the variable that displays the   selected  .
- `supportsOpacity`: A Boolean value that indicates whether the color   picker allows adjustments to the selected color’s opacity; the   default is  .

## See Also

- [init(selection:supportsOpacity:label:)](colorpicker/init(selection:supportsopacity:label:).md)
  Creates an instance that selects a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:))*