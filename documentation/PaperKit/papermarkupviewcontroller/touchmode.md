# PaperMarkupViewController.TouchMode

**Framework**: PaperKit  
**Kind**: enum  
**Role**: Enumeration

The canvas behavior for touches.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum TouchMode
```

## Topics

### Choosing a mode
- [PaperMarkupViewController.TouchMode.selection](./touchmode/selection.md)
  Select strokes/elements on a canvas.
- [PaperMarkupViewController.TouchMode.drawing](./touchmode/drawing.md)
  Draw with the PencilKit tool.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling touch input
- [var directTouchMode: PaperMarkupViewController.TouchMode](./directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var directTouchAutomaticallyDraws: Bool](./directtouchautomaticallydraws.md)
  A Boolean value that indicates whether direct touches automatically draw based on system state.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](./indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/touchmode)*