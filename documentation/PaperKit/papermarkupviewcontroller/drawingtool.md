# drawingTool

**Framework**: PaperKit  
**Kind**: property

The tool used to draw on the canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var drawingTool: any PKTool { get set }
```

#### Discussion

When the touch is a drawing interaction this is the tool that is used to draw.

Default is `PKInkingTool(.pen)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/drawingtool)*