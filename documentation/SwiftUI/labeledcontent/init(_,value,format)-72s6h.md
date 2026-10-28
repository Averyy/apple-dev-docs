# init(_:value:format:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled informational view from a formatted value.

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
init<F>(_ titleResource: LocalizedStringResource, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

Available when `Label` is `Text` and `Content` is `Text`.

**Other overloads**:

```swift
init<F>(_ titleKey: LocalizedStringKey, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
init<S, F>(_ title: S, value: F.FormatInput, format: F) where S : StringProtocol, F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf. See `Text` for more information about localizing strings.

```swift
Form {
    LabeledContent("Age", value: person.age, format: .number)
    LabeledContent("Height", value: person.height,
        format: .measurement(width: .abbreviated))
}
```

## Parameters

- `titleResource`: Text resource for the view’s localized title, that describes the purpose of the view.
- `value`: The value being labeled.
- `format`: A format style of type `F` to convert the underlying value of type `F.FormatInput` to a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:format:)-72s6h)*