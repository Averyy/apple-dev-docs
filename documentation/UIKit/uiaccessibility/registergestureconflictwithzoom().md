# registerGestureConflictWithZoom()

**Framework**: UIKit  
**Kind**: method

Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func registerGestureConflictWithZoom()
```

#### Discussion

Use this function if your application uses multi-finger gestures that conflict with the gestures used by system Zoom (that is, three-finger gestures). When this is the case, the user is presented with the choice of turning off Zoom or continuing.

## See Also

- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](uiaccessibility/focusedelement(using:).md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](uiaccessibility/requestguidedaccesssession(enabled:completionhandler:).md)
  Transitions the app to or from Single App mode asynchronously.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/registergestureconflictwithzoom())*