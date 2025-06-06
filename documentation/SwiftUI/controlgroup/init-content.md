# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

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
nonisolated
init<C, S>(_ title: S, @ViewBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Text>, C : View, S : StringProtocol
```

## Parameters

- `title`: A string that describes the contents of the group.

## See Also

- [init(content: () -> Content)](controlgroup/init(content:).md)
  Creates a new ControlGroup with the specified children
- [init<C, L>(content: () -> C, label: () -> L)](controlgroup/init(content:label:).md)
  Creates a new control group with the specified content and a label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:content:))*