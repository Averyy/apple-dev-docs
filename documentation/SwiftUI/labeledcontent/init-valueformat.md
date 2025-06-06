# init(_:value:format:)

**Framework**: SwiftUI  
**Kind**: init

Creates a labeled informational view from a formatted value.

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
init<F>(_ titleKey: LocalizedStringKey, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

#### Discussion

This initializer creates a [`Text`](text.md) label on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See `Text` for more information about localizing strings.

```swift
Form {
    LabeledContent("Age", value: person.age, format: .number)
    LabeledContent("Height", value: person.height,
        format: .measurement(width: .abbreviated))
}
```

## Parameters

- `titleKey`: The key for the view’s localized title, that describes   the purpose of the view.
- `value`: The value being labeled.
- `format`: A format style of type   to convert the underlying value   of type   to a string representation.

## See Also

- [init(_:content:)](labeledcontent/init(_:content:).md)
  Creates a labeled view that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](labeledcontent/init(content:label:).md)
  Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](labeledcontent/init(_:value:).md)
  Creates a labeled informational view.
- [init(LabeledContentStyleConfiguration)](labeledcontent/init(_:).md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:format:))*