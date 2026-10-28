# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a text view title and an identifier.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0 (renamed: init(_:id:makeContent:))
- iPadOS 14.0+ - Deprecated in 18.0 (renamed: init(_:id:makeContent:))
- Mac Catalyst 14.0+ - Deprecated in 18.0 (renamed: init(_:id:makeContent:))
- macOS 11.0+ - Deprecated in 15.0 (renamed: init(_:id:makeContent:))
- tvOS 14.0+ - Deprecated in 18.0 (renamed: init(_:id:makeContent:))
- visionOS 1.0+ - Deprecated in 2.0 (renamed: init(_:id:makeContent:))
- watchOS 7.0+ - Deprecated in 11.0 (renamed: init(_:id:makeContent:))

> **Deprecated**: Use the initializer which takes an escaping content builder instead.

## Declaration

```swift
nonisolated
init(_ title: Text, id: String, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, id: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, id: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The [`Text`](../text.md) view to use for the group’s title.
- `id`: A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.
- `content`: A closure that creates the content for each instance of the group.

## See Also

### Deprecated
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a window group.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a window group with a text view title.
- [init(id: String, content: () -> Content)](./init%28id,content%29.md)
  Creates a window group with an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:id:content:))*