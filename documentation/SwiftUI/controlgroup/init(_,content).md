# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new control group with the specified content that generates its label from a string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init<C, S>(_ title: S, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Text>, C : View, S : StringProtocol
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<C>(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Text>, C : View
```

```swift
@export(implementation)
nonisolated init<C>(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Text>, C : View
```

## Parameters

- `title`: A string that describes the contents of the group.
- `content`: The content to display.

## See Also

### Creating a control group
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a new ControlGroup with the specified children
- [init<C, L>(content: () -> C, label: () -> L)](./init%28content,label%29.md)
  Creates a new control group with the specified content and a label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:content:))*