# directTouchAutomaticallyDraws

**Framework**: PaperKit  
**Kind**: property

A Boolean value that indicates whether direct touches automatically draw based on system state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var directTouchAutomaticallyDraws: Bool { get set }
```

#### Discussion

Direct touches on the canvas behave as if `directTouchMode = .drawing` when `directTouchAutomaticallyDraws` is true, a `PKToolPicker` is visible, and the “Draw with Finger” system setting is on.

Default is `true`.

## See Also

- [var directTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.
- [PaperMarkupViewController.TouchMode](papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/directtouchautomaticallydraws)*