# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a utility window with a title and identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(_ title: Text, id: String, @ViewBuilder content: () -> Content)
```

#### Discussion

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The   view to use in the utility window’s title bar.   Provide a title that describes the purpose of the utility window.
- `id`: An unique string identifier that you can use to open the utility   window.
- `content`: The view content to display in the utility window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/utilitywindow/init(_:id:content:))*