# resetDetection()

**Framework**: RealityKit  
**Kind**: method

Moves the session state from `.detecting` back to `.ready` to reset the bounding box and prepare to select a new one with a new call to `startDetecting()`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@discardableResult
@MainActor func resetDetection() -> Bool
```

#### Discussion

If the session is not in `.detecting` state this will return false and have no effect.

This call allows the object selection process to be restarted from scratch by the user if the wrong object is automatically selected or the user wants to discard manual bounding box edits and rerun the automatic selection process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/resetdetection())*