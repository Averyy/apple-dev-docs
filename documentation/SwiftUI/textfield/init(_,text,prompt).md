# init(_:text:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a text label generated from a localized title string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, prompt: Text?)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, prompt: Text?)
```

```swift
nonisolated
init<S>(_ title: S, text: Binding<String>, prompt: Text?) where S : StringProtocol
```

## Discussion

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `titleResource`: The localized title of the text field, describing its purpose.
- `text`: The text to display and edit.
- `prompt`: A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.

## See Also

### Creating a text field with a string
- [init(_:text:)](./init%28_,text%29.md)
  Creates a text field with a text label generated from a localized title string.
- [init(text: Binding<String>, prompt: Text?, label: () -> Label)](./init%28text,prompt,label%29.md)
  Creates a text field with a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:prompt:))*