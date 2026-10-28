# init(_:text:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a text label generated from a title string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, text: Binding<String>) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, text: Binding<String>)
```

## Parameters

- `title`: The title of the text view, describing its purpose.
- `text`: The text to display and edit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:)-2laoi)*