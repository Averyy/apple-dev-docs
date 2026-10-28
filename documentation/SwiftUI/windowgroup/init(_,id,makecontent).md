# init(_:id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with a text view title and an identifier.

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
@export(implementation)
nonisolated init(_ title: Text, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, id: String, @ContentBuilder makeContent: @escaping () -> Content) where S : StringProtocol
```

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> ❗ **Important**: The system ignores any text styling that you apply to the [`Text`](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## Parameters

- `title`: The [`Text`](../text.md) view to use for the group’s title.
- `id`: A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.
- `makeContent`: A closure that creates the content for each instance of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:id:makecontent:))*