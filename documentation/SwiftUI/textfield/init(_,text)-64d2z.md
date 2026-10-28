# init(_:text:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a text label generated from a localized title string resource.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, text: Binding<String>)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, text: Binding<String>) where S : StringProtocol
```

## Parameters

- `titleResource`: The localized title of the text field, describing its purpose.
- `text`: The text to display and edit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:)-64d2z)*