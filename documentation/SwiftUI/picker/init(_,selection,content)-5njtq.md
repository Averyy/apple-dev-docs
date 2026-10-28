# init(_:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that generates its label from a string.

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
init<S>(_ title: S, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of selecting an option.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:)-5njtq)*