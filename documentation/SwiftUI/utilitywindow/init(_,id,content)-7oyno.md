# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a utility window with a title and identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
init(_ title: Text, id: String, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, id: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, id: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The [`Text`](../text.md) view to use in the utility window’s title bar. Provide a title that describes the purpose of the utility window.
- `id`: An unique string identifier that you can use to open the utility window.
- `content`: The view content to display in the utility window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/utilitywindow/init(_:id:content:)-7oyno)*