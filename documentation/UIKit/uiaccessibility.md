# UIAccessibility

**Framework**: UIKit  
**Kind**: struct

A namespace for accessibility symbols for UIKit apps.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct UIAccessibility
```

## Topics

### System notifications
- [static let announcementDidFinishNotification: NSNotification.Name](uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.
- [static let elementFocusedNotification: NSNotification.Name](uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
### App notifications
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](uiaccessibility/post(notification:argument:).md)
  Posts a notification to assistive apps.
- [UIAccessibility.Notification](uiaccessibility/notification.md)
  An accessibility notification that an app can send.
### Notification keys
- [static let announcementStringValueUserInfoKey: String](uiaccessibility/announcementstringvalueuserinfokey.md)
  The text of the announcement.
- [static let announcementWasSuccessfulUserInfoKey: String](uiaccessibility/announcementwassuccessfuluserinfokey.md)
  A Boolean value that indicates whether the announcement is successful.
- [static let focusedElementUserInfoKey: String](uiaccessibility/focusedelementuserinfokey.md)
  The element currently in focus by the assistive app.
- [static let unfocusedElementUserInfoKey: String](uiaccessibility/unfocusedelementuserinfokey.md)
  The element previously in focus by the assistive app.
- [static let assistiveTechnologyUserInfoKey: String](uiaccessibility/assistivetechnologyuserinfokey.md)
  The identifier of the assistive app.
### VoiceOver
- [static var isVoiceOverRunning: Bool](uiaccessibility/isvoiceoverrunning.md)
  A Boolean value that indicates whether VoiceOver is in an enabled state.
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](uiaccessibility/voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
### Switch Control
- [static var isSwitchControlRunning: Bool](uiaccessibility/isswitchcontrolrunning.md)
  A Boolean value that indicates whether the Switch Control setting is in an enabled state.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
### AssistiveTouch
- [static var isAssistiveTouchRunning: Bool](uiaccessibility/isassistivetouchrunning.md)
  A Boolean value that indicates whether AssistiveTouch is in an enabled state.
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](uiaccessibility/assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
### Autoplay videos
- [static var isVideoAutoplayEnabled: Bool](uiaccessibility/isvideoautoplayenabled.md)
  A Boolean value that indicates whether the Auto-Play Video Previews setting is in an enabled state.
- [static let videoAutoplayStatusDidChangeNotification: NSNotification.Name](uiaccessibility/videoautoplaystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Auto-Play Video Previews setting changes.
### Bold text
- [static var isBoldTextEnabled: Bool](uiaccessibility/isboldtextenabled.md)
  A Boolean value that indicates whether the Bold Text setting is in an enabled state.
- [static let boldTextStatusDidChangeNotification: NSNotification.Name](uiaccessibility/boldtextstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Bold Text setting changes.
### Button shapes
- [static var buttonShapesEnabled: Bool](uiaccessibility/buttonshapesenabled.md)
  A Boolean value that indicates whether the Button Shapes setting is in an enabled state.
- [static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Button Shapes setting changes.
### Closed captions
- [static var isClosedCaptioningEnabled: Bool](uiaccessibility/isclosedcaptioningenabled.md)
  A Boolean value that indicates whether the Closed Captions + SDH setting is in an enabled state.
- [static let closedCaptioningStatusDidChangeNotification: NSNotification.Name](uiaccessibility/closedcaptioningstatusdidchangenotification.md)
  A notification that UIKit posts when the setting for Closed Captions + SDH changes.
### Cross-fade transitions
- [static var prefersCrossFadeTransitions: Bool](uiaccessibility/preferscrossfadetransitions.md)
  A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.
- [static let prefersCrossFadeTransitionsStatusDidChange: NSNotification.Name](uiaccessibility/preferscrossfadetransitionsstatusdidchange.md)
  A notification that UIKit posts when the system’s Prefer Cross-Fade Transitions setting changes.
### Differentiate without color
- [static var shouldDifferentiateWithoutColor: Bool](uiaccessibility/shoulddifferentiatewithoutcolor.md)
  A Boolean value that indicates whether the Differentiate Without Color setting is in an enabled state.
- [static let differentiateWithoutColorDidChangeNotification: NSNotification.Name](uiaccessibility/differentiatewithoutcolordidchangenotification.md)
  A notification that UIKit posts when the system’s Differentiate Without Color setting changes.
### Grayscale
- [static var isGrayscaleEnabled: Bool](uiaccessibility/isgrayscaleenabled.md)
  A Boolean value that indicates whether the Color Filters and the Grayscale settings are in an enabled state.
- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.
### Guided Access
- [static var isGuidedAccessEnabled: Bool](uiaccessibility/isguidedaccessenabled.md)
  A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static func requestGuidedAccessSession(enabled: Bool, completionHandler: (Bool) -> Void)](uiaccessibility/requestguidedaccesssession(enabled:completionhandler:).md)
  Transitions the app to or from Single App mode asynchronously.
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:).md)
  Enables or disables the specified accessibility features while using Guided Access.
- [static func guidedAccessRestrictionState(forIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate(foridentifier:).md)
  Returns the restriction state for the specified guided access restriction.
- [UIAccessibility.GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate.md)
  Constants that describe the state of a restriction, either allow or deny.
- [static let guidedAccessErrorDomain: String](uiaccessibility/guidedaccesserrordomain.md)
  A string that identifies the Guided Access error domain.
- [UIAccessibility.GuidedAccessError](uiaccessibility/guidedaccesserror.md)
  A Guided Access error.
### Hearing devices
- [static var hearingDevicePairedEar: UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdevicepairedear.md)
  The current pairing status of Made for iPhone hearing devices.
- [static let hearingDevicePairedEarDidChangeNotification: NSNotification.Name](uiaccessibility/hearingdevicepairedeardidchangenotification.md)
  A notification that UIKit posts when there’s a change to the currently paired hearing devices.
### Increase contrast
- [static var isDarkerSystemColorsEnabled: Bool](uiaccessibility/isdarkersystemcolorsenabled.md)
  A Boolean value that indicates whether the Increase Contrast setting is in an enabled state.
- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
### Invert colors
- [static var isInvertColorsEnabled: Bool](uiaccessibility/isinvertcolorsenabled.md)
  A Boolean value that indicates whether the Classic Invert setting is in an enabled state.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.
### Mono audio
- [static var isMonoAudioEnabled: Bool](uiaccessibility/ismonoaudioenabled.md)
  A Boolean value that indicates whether the Mono Audio setting is in an enabled state.
- [static let monoAudioStatusDidChangeNotification: NSNotification.Name](uiaccessibility/monoaudiostatusdidchangenotification.md)
  A notification that UIKit posts when system audio changes from stereo to mono.
### On and off labels
- [static var isOnOffSwitchLabelsEnabled: Bool](uiaccessibility/isonoffswitchlabelsenabled.md)
  A Boolean value that indicates whether the On/Off Labels setting is in an enabled state.
- [static let onOffSwitchLabelsDidChangeNotification: NSNotification.Name](uiaccessibility/onoffswitchlabelsdidchangenotification.md)
  A notification that UIKit posts when the system’s On/Off Labels setting changes.
### Reduce motion
- [static var isReduceMotionEnabled: Bool](uiaccessibility/isreducemotionenabled.md)
  A Boolean value that indicates whether the Reduce Motion setting is in an enabled state.
- [static let reduceMotionStatusDidChangeNotification: NSNotification.Name](uiaccessibility/reducemotionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Motion setting changes.
### Reduce transparency
- [static var isReduceTransparencyEnabled: Bool](uiaccessibility/isreducetransparencyenabled.md)
  A Boolean value that indicates whether the Reduce Transparency setting is in an enabled state.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](uiaccessibility/reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
### Shake to undo
- [static var isShakeToUndoEnabled: Bool](uiaccessibility/isshaketoundoenabled.md)
  A Boolean value that indicates whether the Shake to Undo setting is in an enabled state.
- [static let shakeToUndoDidChangeNotification: NSNotification.Name](uiaccessibility/shaketoundodidchangenotification.md)
  A notification that UIKit posts when the system’s Shake to Undo setting changes.
### Spoken content
- [static var isSpeakScreenEnabled: Bool](uiaccessibility/isspeakscreenenabled.md)
  A Boolean value that indicates whether the Speak Screen setting is in an enabled state.
- [static let speakScreenStatusDidChangeNotification: NSNotification.Name](uiaccessibility/speakscreenstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Screen setting changes.
- [static var isSpeakSelectionEnabled: Bool](uiaccessibility/isspeakselectionenabled.md)
  A Boolean value that indicates whether the Speak Selection setting is in an enabled state.
- [static let speakSelectionStatusDidChangeNotification: NSNotification.Name](uiaccessibility/speakselectionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Selection setting changes.
### Conversions
- [static func convertToScreenCoordinates(UIBezierPath, in: UIView) -> UIBezierPath](uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a.md)
  Converts the specified path object to screen coordinates and returns a new path object with the results.
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
### Convenience functions
- [static func focusedElement(using: UIAccessibility.AssistiveTechnologyIdentifier?) -> Any?](uiaccessibility/focusedelement(using:).md)
  Returns the accessibility element that’s currently in focus by the specified assistive app.
- [static func registerGestureConflictWithZoom()](uiaccessibility/registergestureconflictwithzoom.md)
  Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.
### Constants
- [struct UIAccessibilityTraits](uiaccessibilitytraits.md)
  Constants that describe how an accessibility element behaves.
- [UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md)
  Identifiers for assistive apps.
- [UIAccessibility.HearingDeviceEar](uiaccessibility/hearingdeviceear.md)
  Constants that specify how a person is using a hearing device.
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.
- [enum UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md)
  Constants that describe how to navigate an object’s elements with an assistive app.
- [enum UIAccessibilityScrollDirection](uiaccessibilityscrolldirection.md)
  The direction of a scrolling action.
- [UIAccessibility.ZoomType](uiaccessibility/zoomtype.md)
  The types of system Zoom that can be in effect.
- [UIAccessibility.DirectTouchOptions](uiaccessibility/directtouchoptions.md)
  Constants that configure how VoiceOver produces audio for direct touch areas.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias AXArrayReturnBlock](axarrayreturnblock.md)
- [typealias AXAttributedStringArrayReturnBlock](axattributedstringarrayreturnblock.md)
- [typealias AXAttributedStringReturnBlock](axattributedstringreturnblock.md)
- [typealias AXBoolReturnBlock](axboolreturnblock.md)
- [typealias AXContainerTypeReturnBlock](axcontainertypereturnblock.md)
- [typealias AXCustomActionsReturnBlock](axcustomactionsreturnblock.md)
- [typealias AXCustomRotorsReturnBlock](axcustomrotorsreturnblock.md)
- [typealias AXNavigationStyleReturnBlock](axnavigationstylereturnblock.md)
- [typealias AXObjectReturnBlock](axobjectreturnblock.md)
- [typealias AXPathReturnBlock](axpathreturnblock.md)
- [typealias AXPointReturnBlock](axpointreturnblock.md)
- [typealias AXRectReturnBlock](axrectreturnblock.md)
- [typealias AXStringArrayReturnBlock](axstringarrayreturnblock.md)
- [typealias AXStringReturnBlock](axstringreturnblock.md)
- [typealias AXTextualContextReturnBlock](axtextualcontextreturnblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility)*