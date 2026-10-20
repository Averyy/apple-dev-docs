# UIAccessibility.HearingDeviceEar

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIAccessibilityHearingDeviceEar : NSUInteger;
```

## Topics

### Constants
- [static var left: UIAccessibility.HearingDeviceEar](./hearingdeviceear/left.md)
  A constant that represents the left ear.
- [static var right: UIAccessibility.HearingDeviceEar](./hearingdeviceear/right.md)
  A constant that represents the right ear.
- [static var both: UIAccessibility.HearingDeviceEar](./hearingdeviceear/both.md)
  A constant that represents both ears.
### Initializers
- [init(rawValue: UInt)](./hearingdeviceear/init%28rawvalue%29.md)
  Creates a structure that represents a hearing-device ear with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Convenience functions
- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](./focusedelement%28using%29.md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](./hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [static func registerGestureConflictWithZoom()](./registergestureconflictwithzoom%28%29.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](./requestguidedaccesssession%28enabled,completionhandler%29.md)
  Transitions the app to or from Single App mode asynchronously.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](./zoomfocuschanged%28zoomtype,toframe,in%29.md)
  Notifies the system when the app’s focus changes to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/hearingdeviceear)*