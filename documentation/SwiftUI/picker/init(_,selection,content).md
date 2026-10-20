# init(_:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.

## See Also

### Creating a picker
- [init(selection: Binding<SelectionValue>, content: () -> Content, label: () -> Label)](./init%28selection,content,label%29.md)
  Creates a picker that displays a custom label.
- [init(selection: Binding<SelectionValue>, label: Label, content: () -> Content)](./init%28selection,label,content%29.md)
  Creates a picker that displays a custom label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:))*