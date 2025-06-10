# isEditable

**Framework**: PaperKit  
**Kind**: property

A Boolean value that indicates whether the contents of the canvas is editable.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var isEditable: Bool { get set }
```

#### Discussion

This property controls the ability of the user to edit content. The default value is `true`. Requires coordination with your `MarkupEditViewController` / `MarkupToolbarViewController` to prevent the user from adding new CanvasElements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/iseditable)*