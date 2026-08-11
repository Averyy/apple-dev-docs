# indirectPointerTouchMode

**Framework**: PaperKit  
**Kind**: property

The interaction mode for indirect pointer touches on the canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var indirectPointerTouchMode: PaperMarkupViewController.TouchMode { get set }
```

#### Discussion

Default is `.selection`.

## See Also

- [var directTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var directTouchAutomaticallyDraws: Bool](papermarkupviewcontroller/directtouchautomaticallydraws.md)
  A Boolean value that indicates whether direct touches automatically draw based on system state.
- [PaperMarkupViewController.TouchMode](papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/indirectpointertouchmode)*