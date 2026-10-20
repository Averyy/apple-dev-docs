# hearingDevicePairedEar

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The current pairing status of Made for iPhone hearing devices.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar { get }
```

```c
extern UIAccessibilityHearingDeviceEar UIAccessibilityHearingDevicePairedEar();
```

## See Also

### Convenience functions
- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](./focusedelement%28using%29.md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [UIAccessibility.HearingDeviceEar](./hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [static func registerGestureConflictWithZoom()](./registergestureconflictwithzoom%28%29.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](./requestguidedaccesssession%28enabled,completionhandler%29.md)
  Transitions the app to or from Single App mode asynchronously.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](./zoomfocuschanged%28zoomtype,toframe,in%29.md)
  Notifies the system when the app’s focus changes to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/hearingdevicepairedear)*