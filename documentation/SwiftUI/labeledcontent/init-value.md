# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init

Creates a labeled informational view.

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
init<S1, S2>(_ title: S1, value: S2) where S1 : StringProtocol, S2 : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](text.md) label on your behalf, and treats the title similar to [`init(_:)`](text/init(_:).md). See `Text` for more information about localizing strings.

```swift
Form {
    ForEach(person.pet) { pet in
        LabeledContent(pet.species, value: pet.name)
    }
}
```

## Parameters

- `title`: A string that describes the purpose of the view.
- `value`: The value being labeled.

## See Also

- [init(_:content:)](labeledcontent/init(_:content:).md)
  Creates a labeled view that generates its label from a localized string key.
- [init(content: () -> Content, label: () -> Label)](labeledcontent/init(content:label:).md)
  Creates a standard labeled element, with a view that conveys the value of the element and a label.
- [init(_:value:format:)](labeledcontent/init(_:value:format:).md)
  Creates a labeled informational view from a formatted value.
- [init(LabeledContentStyleConfiguration)](labeledcontent/init(_:).md)
  Creates labeled content based on a labeled content style configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontent/init(_:value:))*