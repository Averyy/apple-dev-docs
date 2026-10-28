# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled informational view.

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
init<S>(_ titleResource: LocalizedStringResource, value: S) where S : StringProtocol
```

Available when `Label` is `Text` and `Content` is `Text`.

**Other overloads**:

```swift
init<S1, S2>(_ title: S1, value: S2) where S1 : StringProtocol, S2 : StringProtocol
```

```swift
init<S>(_ titleKey: LocalizedStringKey, value: S) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) label on your behalf. See `Text` for more information about localizing strings.

```swift
Form {
    LabeledContent("Name", value: person.name)
}
```

In some contexts, this text will be selectable by default.

## Parameters

- `titleResource`: Text resource for the view’s localized title, that describes the purpose of the view.
- `value`: The value being labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:)-90lg7)*