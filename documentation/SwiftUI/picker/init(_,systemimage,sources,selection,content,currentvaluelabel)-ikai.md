# init(_:systemImage:sources:selection:content:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that accepts a custom current value label and generates its label from a localized string key.

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
nonisolated init<C>(_ titleKey: LocalizedStringKey, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<C, S>(_ title: S, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>
```

```swift
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where C : RandomAccessCollection, C.Element == Binding<SelectionValue>
```

## Parameters

- `titleKey`: A localized string key that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `sources`: A collection of values used as the source for displaying the Picker’s selection.
- `selection`: The key path of the values that determines the currently-selected options. When a user selects an option from the picker, the values at the key path of all items in the `sources` collection are updated with the selected option.
- `content`: A view that contains the set of options.
- `currentValueLabel`: A view that represents the current value of the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:currentvaluelabel:)-ikai)*