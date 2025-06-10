# UIAccessibility.HearingDeviceEar

**Framework**: UIKit  
**Kind**: struct

Constants that specify how a person is using a hearing device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct HearingDeviceEar
```

## Topics

### Constants
- [static var left: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear/left.md)
  A constant that represents the left ear.
- [static var right: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear/right.md)
  A constant that represents the right ear.
- [static var both: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear/both.md)
  A constant that represents both ears.
### Initializers
- [init(rawValue: UInt)](uiaccessibility/hearingdeviceear/init(rawvalue:).md)
  Creates a structure that represents a hearing-device ear with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](uiaccessibility/focusedelement(using:).md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [static func registerGestureConflictWithZoom()](uiaccessibility/registergestureconflictwithzoom.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](uiaccessibility/requestguidedaccesssession(enabled:completionhandler:).md)
  Transitions the app to or from Single App mode asynchronously.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/hearingdeviceear)*