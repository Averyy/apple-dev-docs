# init(selection:label:content:)

**Framework**: SwiftUI  
**Kind**: init

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
nonisolated
init(selection: Binding<SelectionValue>, label: Label, @ContentBuilder content: () -> Content)
```

## Parameters

- `selection`: A binding to a property that determines the currently-selected option.
- `label`: A view that describes the purpose of selecting an option.
- `content`: A view that contains the set of options.

## See Also

- [init(_:selection:content:)](picker/init(_:selection:content:).md)
  Creates a picker that generates its label from a localized string resource.
- [init(selection: Binding<SelectionValue>, content: () -> Content, label: () -> Label)](picker/init(selection:content:label:).md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(selection:label:content:))*