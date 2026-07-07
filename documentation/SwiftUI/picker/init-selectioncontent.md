# init(_:selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that generates its label from a localized string resource.

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.

## See Also

- [init(selection: Binding<SelectionValue>, content: () -> Content, label: () -> Label)](picker/init(selection:content:label:).md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:))*