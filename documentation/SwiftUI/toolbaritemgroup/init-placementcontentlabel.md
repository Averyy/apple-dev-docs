# init(placement:content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toolbar item group with the specified placement, content, and a label describing that content.

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
nonisolated
init<C, L>(placement: ToolbarItemPlacement = .automatic, @ViewBuilder content: () -> C, @ViewBuilder label: () -> L) where Content == LabeledToolbarItemGroupContent<C, L>, C : View, L : View
```

#### Discussion

A toolbar item group provided a label wraps its content within a [`ControlGroup`](controlgroup.md) which allows the content to collapse down into a menu that presents its content based on available space.

## Parameters

- `placement`: Which section of the toolbar   the item should be placed in.
- `content`: The content of the item.
- `label`: The label describing the content of the item.

## See Also

- [init(placement: ToolbarItemPlacement, content: () -> Content)](toolbaritemgroup/init(placement:content:).md)
  Creates a toolbar item group with a specified placement and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemgroup/init(placement:content:label:))*