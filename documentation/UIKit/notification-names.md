# Notification names

**Framework**: UIKit

The names of notifications that the accessibility system generates.

## Topics

### UI changes
- [static let screenChanged: UIAccessibility.Notification](uiaccessibility/notification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let layoutChanged: UIAccessibility.Notification](uiaccessibility/notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let pageScrolled: UIAccessibility.Notification](uiaccessibility/notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let switchControlStatusDidChangeNotification: NSNotification.Name](uiaccessibility/switchcontrolstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Switch Control setting changes.
- [static let elementFocusedNotification: NSNotification.Name](uiaccessibility/elementfocusednotification.md)
  A notification that UIKit posts when an assistive app focuses on an accessibility element.
- [static let reduceTransparencyStatusDidChangeNotification: NSNotification.Name](uiaccessibility/reducetransparencystatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Transparency setting changes.
- [static let buttonShapesEnabledStatusDidChangeNotification: NSNotification.Name](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Button Shapes setting changes.
### VoiceOver
- [static let announcement: UIAccessibility.Notification](uiaccessibility/notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let voiceOverStatusDidChangeNotification: NSNotification.Name](uiaccessibility/voiceoverstatusdidchangenotification.md)
  A notification that UIKit posts when VoiceOver starts or stops.
- [static let announcementDidFinishNotification: NSNotification.Name](uiaccessibility/announcementdidfinishnotification.md)
  A notification that UIKit posts when the system finishes reading an announcement.
- [let UIAccessibilityVoiceOverStatusChanged: String](uiaccessibilityvoiceoverstatuschanged.md)
  A notification that UIKit posts when VoiceOver starts or stops.
### Text
- [static let boldTextStatusDidChangeNotification: NSNotification.Name](uiaccessibility/boldtextstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Bold Text setting changes.
- [static let closedCaptioningStatusDidChangeNotification: NSNotification.Name](uiaccessibility/closedcaptioningstatusdidchangenotification.md)
  A notification that UIKit posts when the setting for Closed Captions + SDH changes.
### Colors
- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.
### Assistive apps
- [static let assistiveTouchStatusDidChangeNotification: NSNotification.Name](uiaccessibility/assistivetouchstatusdidchangenotification.md)
  A notification that indicates a change in the status of AssistiveTouch.
- [static let guidedAccessStatusDidChangeNotification: NSNotification.Name](uiaccessibility/guidedaccessstatusdidchangenotification.md)
  A notification that indicates when a Guided Access session starts or ends.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md)
  Identifiers for assistive apps.
### Audio and speech
- [static let monoAudioStatusDidChangeNotification: NSNotification.Name](uiaccessibility/monoaudiostatusdidchangenotification.md)
  A notification that UIKit posts when system audio changes from stereo to mono.
- [static let speakScreenStatusDidChangeNotification: NSNotification.Name](uiaccessibility/speakscreenstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Screen setting changes.
- [static let speakSelectionStatusDidChangeNotification: NSNotification.Name](uiaccessibility/speakselectionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Speak Selection setting changes.
- [static let hearingDevicePairedEarDidChangeNotification: NSNotification.Name](uiaccessibility/hearingdevicepairedeardidchangenotification.md)
  A notification that UIKit posts when there’s a change to the currently paired hearing devices.
### Motion
- [static let reduceMotionStatusDidChangeNotification: NSNotification.Name](uiaccessibility/reducemotionstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Reduce Motion setting changes.
- [static let shakeToUndoDidChangeNotification: NSNotification.Name](uiaccessibility/shaketoundodidchangenotification.md)
  A notification that UIKit posts when the system’s Shake to Undo setting changes.

## See Also

- [Notification dictionary keys](notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](uiaccessibility/post(notification:argument:).md)
  Posts a notification to assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/notification-names)*