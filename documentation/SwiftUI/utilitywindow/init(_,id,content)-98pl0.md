# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a utility window with a title string and identifier.

**Availability**:
- macOS 15.0+

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

## Parameters

- `title`: A string to use in the utility window’s title bar. Provide a title that describes the purpose of the utility window.
- `id`: An unique string identifier that you can use to open the utility window.
- `content`: The view content to display in the utility window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/utilitywindow/init(_:id:content:)-98pl0)*