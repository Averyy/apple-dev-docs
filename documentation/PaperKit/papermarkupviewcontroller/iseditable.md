# isEditable

**Framework**: PaperKit  
**Kind**: property

A Boolean value that indicates whether a person can edit the canvas contents.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var isEditable: Bool { get set }
```

#### Discussion

This property controls whether a person can edit content. The default value is `true`. Coordinate this property with your `MarkupEditViewController` or `MarkupToolbarViewController` to prevent people from adding new canvas elements.

## See Also

- [var drawingTool: any PKTool](papermarkupviewcontroller/drawingtool.md)
  The tool for drawing on the canvas.
- [var isRulerActive: Bool](papermarkupviewcontroller/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/iseditable)*