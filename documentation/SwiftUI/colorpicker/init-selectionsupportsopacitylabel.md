# init(selection:supportsOpacity:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects a color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(selection: Binding<CGColor>, supportsOpacity: Bool = true, @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: A   to the variable that displays the   selected  .
- `supportsOpacity`: A Boolean value that indicates whether the color   picker allows adjusting the selected color’s opacity; the default   is  .
- `label`: A view that describes the use of the selected color.   The system color picker UI sets it’s title using the text from   this view.

## See Also

- [init(_:selection:supportsOpacity:)](colorpicker/init(_:selection:supportsopacity:).md)
  Creates a color picker with a text label generated from a title string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorpicker/init(selection:supportsopacity:label:))*