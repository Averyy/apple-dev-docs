# init(_:value:format:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text` and `Content` is `Text`.

**Other overloads**:

```swift
init<F>(_ titleResource: LocalizedStringResource, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
init<S, F>(_ title: S, value: F.FormatInput, format: F) where S : StringProtocol, F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See `Text` for more information about localizing strings.

```swift
Form {
    LabeledContent("Age", value: person.age, format: .number)
    LabeledContent("Height", value: person.height,
        format: .measurement(width: .abbreviated))
}
```

## Parameters

- `titleKey`: The key for the view’s localized title, that describes the purpose of the view.
- `value`: The value being labeled.
- `format`: A format style of type `F` to convert the underlying value of type `F.FormatInput` to a string representation.

## See Also

### Creating labeled content
- [init(_:content:)](./init%28_,content%29.md)
  Creates a labeled view that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:)](./init%28_,value%29.md)
  Creates a labeled informational view.
- [init(LabeledContentStyleConfiguration)](./init%28_%29.md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:format:))*