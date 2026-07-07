# directTouchMode

**Framework**: PaperKit  
**Kind**: property

The interaction mode for direct touches on the canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var directTouchMode: PaperMarkupViewController.TouchMode { get set }
```

#### Discussion

To control automatic behavior for direct touches based on system state, see `directTouchAutomaticallyDraws`. Default is `.selection`.

## See Also

- [var directTouchAutomaticallyDraws: Bool](papermarkupviewcontroller/directtouchautomaticallydraws.md)
  A Boolean value that indicates whether direct touches automatically draw based on system state.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.
- [PaperMarkupViewController.TouchMode](papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/directtouchmode)*