# focusedElement(using:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the accessibility element that’s currently in focus by the specified assistive app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func focusedElement(using assistiveTechnologyIdentifier: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?
```

```c
extern idUIAccessibilityFocusedElement(UIAccessibilityAssistiveTechnologyIdentifier assistiveTechnologyIdentifier);
```

#### Return Value

The element that is currently focused by the specified assistive technology or the element that was most recently focused, if no technology is specified.

## See Also

### Convenience functions
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](./hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [UIAccessibility.HearingDeviceEar](./hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [static func registerGestureConflictWithZoom()](./registergestureconflictwithzoom%28%29.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](./requestguidedaccesssession%28enabled,completionhandler%29.md)
  Transitions the app to or from Single App mode asynchronously.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](./zoomfocuschanged%28zoomtype,toframe,in%29.md)
  Notifies the system when the app’s focus changes to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/focusedelement(using:))*