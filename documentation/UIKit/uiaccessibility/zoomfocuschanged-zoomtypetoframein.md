# zoomFocusChanged(zoomType:toFrame:in:)

**Framework**: UIKit  
**Kind**: method

Notifies the system when the app’s focus changes to a new location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func zoomFocusChanged(zoomType type: UIAccessibility.ZoomType, toFrame frame: CGRect, in view: UIView)
```

## Parameters

- `type`: A   constant that identifies the type of Zoom.
- `frame`: The frame that’s currently zoomed, in screen coordinates.
- `view`: The view that contains the zoomed frame.

## See Also

- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](uiaccessibility/focusedelement(using:).md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [static func registerGestureConflictWithZoom()](uiaccessibility/registergestureconflictwithzoom.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](uiaccessibility/requestguidedaccesssession(enabled:completionhandler:).md)
  Transitions the app to or from Single App mode asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:))*