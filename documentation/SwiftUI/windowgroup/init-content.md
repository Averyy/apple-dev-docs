# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a window group with a text view title.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(_ title: Text, @ViewBuilder content: () -> Content)
```

#### Discussion

The window group uses the given view as a template to form the content of each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

The system ignores any text styling that you apply to the [`Text`](text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The   view to use for the group’s title.
- `content`: A closure that creates the content for each instance   of the group.

## See Also

- [init(content: () -> Content)](windowgroup/init(content:).md)
  Creates a window group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:content:))*