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
init<S, F>(_ title: S, value: F.FormatInput, format: F) where S : StringProtocol, F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

Available when `Label` is `Text` and `Content` is `Text`.

**Other overloads**:

```swift
init<F>(_ titleKey: LocalizedStringKey, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

```swift
init<F>(_ titleResource: LocalizedStringResource, value: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). See `Text` for more information about localizing strings.

```swift
Form {
    Section("Downloads") {
        ForEach(download) { file in
            LabeledContent(file.name, value: file.downloadSize,
                format: .byteCount(style: .file))
       }
    }
}
```

## Parameters

- `title`: A string that describes the purpose of the view.
- `value`: The value being labeled.
- `format`: A format style of type `F` to convert the underlying value of type `F.FormatInput` to a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:format:)-9xjga)*