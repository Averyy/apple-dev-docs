# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window with a title string and an identifier.

**Availability**:
- macOS 13.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, id: String, @ContentBuilder content: () -> Content) where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ title: Text, id: String, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, id: String, @ContentBuilder content: () -> Content)
```

## Discussion

The window displays the view that you specify.

## Parameters

- `title`: A string to use for the window’s title in system menus and in the window’s title bar. Provide a title that describes the purpose of the window.
- `id`: A unique string identifier that you can use to open the window.
- `content`: The view content to display in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/window/init(_:id:content:)-7fkt9)*