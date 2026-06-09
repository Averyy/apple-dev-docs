# realityViewCameraControls(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds gestures that control the position and direction of a virtual camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency func realityViewCameraControls(_ controls: CameraControls) -> some View
```

#### Discussion

You can use a drag gesture from a mouse, trackpad, or screen touches with iOS and iPadOS devices to `.tilt`, `.pan`, `.orbit`, or `.dolly` a virtual camera.

## See Also

- [var realityViewCameraControls: CameraControls](environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [func realityViewLayoutBehavior(RealityViewLayoutOption) -> some View](view/realityviewlayoutbehavior(_:).md)
  A view modifier that controls the frame sizing and content alignment behavior for `RealityView`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/realityviewcameracontrols(_:))*