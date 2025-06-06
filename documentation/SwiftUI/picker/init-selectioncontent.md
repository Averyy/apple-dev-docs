# init(_:selection:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that generates its label from a localized string key.

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
init(_ titleKey: LocalizedStringKey, selection: Binding<SelectionValue>, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleKey`: A localized string key that describes the purpose of   selecting an option.
- `selection`: A binding to a property that determines the   currently-selected option.
- `content`: A view that contains the set of options.

## See Also

- [init(selection: Binding<SelectionValue>, content: () -> Content, label: () -> Label)](picker/init(selection:content:label:).md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:))*