# menuStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for menus within this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func menuStyle<S>(_ style: S) -> some View where S : MenuStyle
```

#### Discussion

To set a specific style for all menu instances within a view, use the `menuStyle(_:)` modifier:

```swift
Menu("PDF") {
    Button("Open in Preview", action: openInPreview)
    Button("Save as PDF", action: saveAsPDF)
}
.menuStyle(ButtonMenuStyle())
```

## See Also

- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)
  Improve your app by populating menus with controls and organizing your content intuitively.
- [struct Menu](menu.md)
  A control for presenting a menu of actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/menustyle(_:))*