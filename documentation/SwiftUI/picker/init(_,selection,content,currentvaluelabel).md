# init(_:selection:content:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that generates its label from a localized string resource and accepts a custom current value label.

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.
- `currentValueLabel`: A view that represents the current value of the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:currentvaluelabel:))*