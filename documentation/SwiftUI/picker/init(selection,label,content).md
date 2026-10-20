# init(selection:label:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that displays a custom label.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: Picker(selection:content:label:))

> **Deprecated**: Use [`init(selection:content:label:)`](./init%28selection,content,label%29.md) instead.

## Declaration

```swift
nonisolated
init(selection: Binding<SelectionValue>, label: Label, @ContentBuilder content: () -> Content)
```

Available when `Label` conforms to `View`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

## Parameters

- `selection`: A binding to a property that determines the currently-selected option.
- `label`: A view that describes the purpose of selecting an option.
- `content`: A view that contains the set of options.

## See Also

### Creating a picker
- [init(_:selection:content:)](./init%28_,selection,content%29.md)
  Creates a picker that generates its label from a localized string resource.
- [init(selection: Binding<SelectionValue>, content: () -> Content, label: () -> Label)](./init%28selection,content,label%29.md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(selection:label:content:))*