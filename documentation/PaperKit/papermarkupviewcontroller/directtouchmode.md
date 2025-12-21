# directTouchMode

**Framework**: PaperKit  
**Kind**: property

The interaction mode for direct touches on the canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var directTouchMode: PaperMarkupViewController.TouchMode { get set }
```

#### Discussion

To control automatic behavior for direct touches based on system state, see `directTouchAutomaticallyDraws`. Default is `.selection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/directtouchmode)*