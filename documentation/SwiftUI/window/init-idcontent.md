# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a window with a title and an identifier.

**Availability**:
- macOS 13.0+
- visionOS 26.0+

## Declaration

```swift
init(_ title: Text, id: String, @ViewBuilder content: () -> Content)
```

#### Discussion

The window displays the view that you specify.

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The   view to use for the window’s title in system   menus and in the window’s title bar. Provide a title that   describes the purpose of the window.
- `id`: A unique string identifier that you can use to   open the window.
- `content`: The view content to display in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/window/init(_:id:content:))*