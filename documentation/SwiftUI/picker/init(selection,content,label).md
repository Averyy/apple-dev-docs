# init(selection:content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that displays a custom label.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
nonisolated init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

## Parameters

- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.
- `label`: A view that describes the purpose of selecting an option.

## See Also

### Creating a picker
- [init(_:selection:content:)](./init%28_,selection,content%29.md)
  Creates a picker that generates its label from a localized string resource.
- [init(selection: Binding<SelectionValue>, label: Label, content: () -> Content)](./init%28selection,label,content%29.md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(selection:content:label:))*