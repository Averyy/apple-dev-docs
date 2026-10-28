# init(_:image:selection:content:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that accepts a custom current value label and generates its label from a localized string key and image resource.

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
nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

```swift
nonisolated
init<S>(_ title: S, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: A localized string resource that describes the purpose of selecting an option.
- `image`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.
- `currentValueLabel`: A view that represents the current value of the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:image:selection:content:currentvaluelabel:))*