# init(selection:content:label:)

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
init(selection: Binding<SelectionValue>, @ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: A binding to a property that determines the   currently-selected option.
- `content`: A view that contains the set of options.
- `label`: A view that describes the purpose of selecting an option.

## See Also

- [init(_:selection:content:)](picker/init(_:selection:content:).md)
  Creates a picker that generates its label from a localized string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(selection:content:label:))*