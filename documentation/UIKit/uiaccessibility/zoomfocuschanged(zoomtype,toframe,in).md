# zoomFocusChanged(zoomType:toFrame:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Notifies the system when the app’s focus changes to a new location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func zoomFocusChanged(zoomType type: UIAccessibility.ZoomType, toFrame frame: CGRect, in view: UIView)
```

```c
extern void UIAccessibilityZoomFocusChanged(UIAccessibilityZoomType type, CGRect frame, UIView *view);
```

## Parameters

- `type`: A `UIKit Functions` constant that identifies the type of Zoom.
- `frame`: The frame that’s currently zoomed, in screen coordinates.
- `view`: The view that contains the zoomed frame.

## See Also

### Convenience functions
- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](./focusedelement%28using%29.md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](./hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [UIAccessibility.HearingDeviceEar](./hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [static func registerGestureConflictWithZoom()](./registergestureconflictwithzoom%28%29.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](./requestguidedaccesssession%28enabled,completionhandler%29.md)
  Transitions the app to or from Single App mode asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:))*