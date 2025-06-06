# init(placement:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toolbar item group with a specified placement and content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(placement: ToolbarItemPlacement = .automatic, @ViewBuilder content: () -> Content)
```

#### Discussion

- placement: Which section of the toolbar all of its vended `ToolbarItem`s should be placed in.
- content: The content of the group. Each view specified in the `ViewBuilder` will be given its own `ToolbarItem` in the toolbar.

## See Also

- [init<C, L>(placement: ToolbarItemPlacement, content: () -> C, label: () -> L)](toolbaritemgroup/init(placement:content:label:).md)
  Creates a toolbar item group with the specified placement, content, and a label describing that content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemgroup/init(placement:content:))*