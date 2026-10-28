# init(_:text:axis:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a preferred axis and a text label generated from a localized title string resource.

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
nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, axis: Axis)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, axis: Axis)
```

```swift
nonisolated
init<S>(_ title: S, text: Binding<String>, axis: Axis) where S : StringProtocol
```

## Discussion

Specify a preferred axis in which the text field should scroll its content when it does not fit in the available space. Depending on the style of the field, this axis may not be respected.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `titleResource`: The localized title of the text field, describing its purpose.
- `text`: The text to display and edit.
- `axis`: The axis in which to scroll text when it doesn’t fit in the available space.

## See Also

### Creating a scrollable text field
- [init(_:text:prompt:axis:)](./init%28_,text,prompt,axis%29.md)
  Creates a text field with a preferred axis and a text label generated from a localized title string resource.
- [init(text: Binding<String>, prompt: Text?, axis: Axis, label: () -> Label)](./init%28text,prompt,axis,label%29.md)
  Creates a text field with a preferred axis and a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:axis:))*