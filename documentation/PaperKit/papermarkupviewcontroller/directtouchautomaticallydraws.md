# directTouchAutomaticallyDraws

**Framework**: PaperKit  
**Kind**: property

A Boolean value that indicates that direct touches should automatically draw based on system state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var directTouchAutomaticallyDraws: Bool { get set }
```

#### Discussion

Direct touches on the canvas behave as if `directTouchMode = .drawing` when `directTouchAutomaticallyDraws` is true, a `PKToolPicker` is visible, and the “Draw with Finger” system setting is on.

Default is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/directtouchautomaticallydraws)*