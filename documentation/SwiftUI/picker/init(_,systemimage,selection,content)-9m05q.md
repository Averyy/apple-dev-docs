# init(_:systemImage:selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that generates its label from a localized string resource and system image.

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
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
nonisolated init<S>(_ title: S, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:selection:content:)-9m05q)*