# drawingTool

**Framework**: PaperKit  
**Kind**: property

The tool for drawing on the canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var drawingTool: any PKTool { get set }
```

#### Discussion

When a touch is a drawing interaction, the canvas uses this tool to draw.

Default is `PKInkingTool(.pen)`.

## See Also

- [var isEditable: Bool](papermarkupviewcontroller/iseditable.md)
  A Boolean value that indicates whether a person can edit the canvas contents.
- [var isRulerActive: Bool](papermarkupviewcontroller/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/drawingtool)*