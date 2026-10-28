# init(_:systemImage:selection:content:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that accepts a custom current value and generates its label from a string and system image.

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
nonisolated init<S>(_ title: S, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where S : StringProtocol
```

Available when `Label` is `Label<Text, Image>`, `SelectionValue` conforms to `Hashable`, and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

## Parameters

- `title`: A string that describes the purpose of selecting an option.
- `systemImage`: The name of the image resource to lookup.
- `selection`: A binding to a property that determines the currently-selected option.
- `content`: A view that contains the set of options.
- `currentValueLabel`: A view that represents the current value of the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:selection:content:currentvaluelabel:)-46wgz)*