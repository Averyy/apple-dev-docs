# init(_:selection:content:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that generates its label from a string and accepts a custom current value label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where S : StringProtocol
```

Available when `Label` is `Text`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `title`: A string that describes the purpose of selecting an option.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.
- `currentValueLabel`: A view that represents the current value of the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:currentvaluelabel:)-53raj)*