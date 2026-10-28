# init(_:text:prompt:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a secure field with a prompt generated from a `Text`.

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

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## Parameters

- `titleResource`: Text resource for the field’s localized title. The title describes the purpose of the field.
- `text`: A binding to the text that the field displays and edits.
- `prompt`: A [`Text`](../text.md) view that represents the secure field’s prompt. The prompt provides guidance on what people should type into the secure field.

## See Also

### Creating a secure text field
- [init(_:text:)](./init%28_,text%29.md)
  Creates a secure field with a prompt generated from a `Text`.
- [init(text: Binding<String>, prompt: Text?, label: () -> Label)](./init%28text,prompt,label%29.md)
  Creates a secure field with a prompt generated from a `Text`.
- [init(_:text:onCommit:)](./init%28_,text,oncommit%29.md)
  Creates an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(_:text:prompt:))*