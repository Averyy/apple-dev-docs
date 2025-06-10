# menuStyle(_:)

**Framework**: App Intents  
**Kind**: method

Sets the style for menus within this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS ?+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/menustyle(_:))*