# init(_:text:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a text label generated from a title string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, text: Binding<String>, prompt: Text?) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, prompt: Text?)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, prompt: Text?)
```

## Discussion

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `title`: The title of the text view, describing its purpose.
- `text`: The text to display and edit.
- `prompt`: A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:prompt:)-4kzyv)*