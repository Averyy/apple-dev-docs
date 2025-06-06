# Accessibility for UIKit

**Framework**: UIKit

Make your UIKit apps accessible to everyone who uses iOS and tvOS.

#### Overview

Making your app accessible means making it usable by everyone. By designing your app with accessibility in mind, you make it possible for everyone to enjoy your app. For more information, see [`Accessibility`](https://developer.apple.com/documentation/Accessibility).

UIKit controls and views come with built-in accessibility, providing an accessible user experience by default. Typically, you don’t need to do extra work to enable the standard accessibility features.

In some cases, you might want to modify the default values to better represent your app, to provide additional context, or to modify the user’s flow through the app. UIKit makes these customizations straightforward, involving a few lines of code or Interface Builder adjustments as you define your user interface. For more information about customizing accessibility for UIKit elements, see [`UIAccessibility`](uiaccessibility-protocol.md).

If your app contains custom user interface elements that don’t inherit from [`UIView`](uiview.md) or one of the other UIKit classes with built-in accessibility, make those elements accessible by subclassing [`UIAccessibilityElement`](uiaccessibilityelement.md).

If you build your app with SwiftUI, see [`Accessibility modifiers`](https://developer.apple.com/documentation/SwiftUI/View-Accessibility).

## Topics

### Essentials
- [UIAccessibility](uiaccessibility-protocol.md)
  A set of methods that provides accessibility information about views and controls in an app’s user interface.
- [UIAccessibilityContainer](uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)
  Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.
### Behaviors
- [UIAccessibilityFocus](../ObjectiveC/uiaccessibilityfocus.md)
  An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [protocol UIAccessibilityIdentification](uiaccessibilityidentification.md)
  Methods that associate a unique identifier with elements in your user interface.
- [protocol UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md)
  Methods to implement for an object that represents content that users read, such as a book or an article.
- [protocol UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)
  Methods to determine when to adjust images for different content size categories.
- [struct UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md)
  Constants that describe a named context that helps identify and classify the type of text inside an element.
### Guided Access
- [static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler: (Bool, (any Error)?) -> Void)](uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:).md)
  Enables or disables the specified accessibility features while using Guided Access.
- [struct UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature.md)
  Constants that describe accessibility features for Guided Access.
- [UIAccessibility.GuidedAccessError.Code](uiaccessibility/guidedaccesserror/code.md)
  Error codes for Guided Access.
### Actions
- [UIAccessibilityAction](../ObjectiveC/uiaccessibilityaction.md)
  A set of methods that accessibility elements can use to support specific actions.
- [class UIAccessibilityCustomAction](uiaccessibilitycustomaction.md)
  A custom action to perform on an accessible object.
- [UIAccessibilityCustomAction.Handler](uiaccessibilitycustomaction/handler.md)
  A closure type that defines a handler to perform for an action.
- [Delivering an exceptional accessibility experience](../Accessibility/delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
### Elements
- [class UIAccessibilityElement](uiaccessibilityelement.md)
  An element that should be accessible to users with disabilities, but that isn’t accessible by default.
- [protocol UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for a scroll view.
- [protocol UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for individual components of a picker view.
### Containers
- [protocol UIAccessibilityContainerDataTable](uiaccessibilitycontainerdatatable.md)
  Methods that convey information about the contents of a table.
- [protocol UIAccessibilityContainerDataTableCell](uiaccessibilitycontainerdatatablecell.md)
  Methods that provide the location of a cell in a table.
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.
### Navigation
- [class UIAccessibilityCustomRotor](uiaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related element.
- [class UIAccessibilityCustomRotorItemResult](uiaccessibilitycustomrotoritemresult.md)
  A target element that a custom rotor references.
- [class UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md)
  The search parameters that help determine the next matching custom rotor item result.
### Drag and drop support
- [class UIAccessibilityLocationDescriptor](uiaccessibilitylocationdescriptor.md)
  An accessibility descriptor for a specific geometric point of interest within a view, for use by assistive apps.
### Notifications
- [Notification names](notification-names.md)
  The names of notifications that the accessibility system generates.
- [Notification dictionary keys](notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](uiaccessibility/post(notification:argument:).md)
  Posts a notification to assistive apps.
### Conversions
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
- [static func convertToScreenCoordinates(UIBezierPath, in: UIView) -> UIBezierPath](uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a.md)
  Converts the specified path object to screen coordinates and returns a new path object with the results.
### Convenience functions
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
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.
### Capabilities
- [static var isAssistiveTouchRunning: Bool](uiaccessibility/isassistivetouchrunning.md)
  A Boolean value that indicates whether AssistiveTouch is in an enabled state.
- [static var isVoiceOverRunning: Bool](uiaccessibility/isvoiceoverrunning.md)
  A Boolean value that indicates whether VoiceOver is in an enabled state.
- [static var isSwitchControlRunning: Bool](uiaccessibility/isswitchcontrolrunning.md)
  A Boolean value that indicates whether the Switch Control setting is in an enabled state.
- [static var isShakeToUndoEnabled: Bool](uiaccessibility/isshaketoundoenabled.md)
  A Boolean value that indicates whether the Shake to Undo setting is in an enabled state.
- [static var isClosedCaptioningEnabled: Bool](uiaccessibility/isclosedcaptioningenabled.md)
  A Boolean value that indicates whether the Closed Captions + SDH setting is in an enabled state.
- [static var isBoldTextEnabled: Bool](uiaccessibility/isboldtextenabled.md)
  A Boolean value that indicates whether the Bold Text setting is in an enabled state.
- [static var isDarkerSystemColorsEnabled: Bool](uiaccessibility/isdarkersystemcolorsenabled.md)
  A Boolean value that indicates whether the Increase Contrast setting is in an enabled state.
- [static var isGrayscaleEnabled: Bool](uiaccessibility/isgrayscaleenabled.md)
  A Boolean value that indicates whether the Color Filters and the Grayscale settings are in an enabled state.
- [static var isGuidedAccessEnabled: Bool](uiaccessibility/isguidedaccessenabled.md)
  A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [static var isInvertColorsEnabled: Bool](uiaccessibility/isinvertcolorsenabled.md)
  A Boolean value that indicates whether the Classic Invert setting is in an enabled state.
- [static var isMonoAudioEnabled: Bool](uiaccessibility/ismonoaudioenabled.md)
  A Boolean value that indicates whether the Mono Audio setting is in an enabled state.
- [static var isReduceMotionEnabled: Bool](uiaccessibility/isreducemotionenabled.md)
  A Boolean value that indicates whether the Reduce Motion setting is in an enabled state.
- [static var isReduceTransparencyEnabled: Bool](uiaccessibility/isreducetransparencyenabled.md)
  A Boolean value that indicates whether the Reduce Transparency setting is in an enabled state.
- [static var isSpeakScreenEnabled: Bool](uiaccessibility/isspeakscreenenabled.md)
  A Boolean value that indicates whether the Speak Screen setting is in an enabled state.
- [static var isSpeakSelectionEnabled: Bool](uiaccessibility/isspeakselectionenabled.md)
  A Boolean value that indicates whether the Speak Selection setting is in an enabled state.
- [static var isOnOffSwitchLabelsEnabled: Bool](uiaccessibility/isonoffswitchlabelsenabled.md)
  A Boolean value that indicates whether the On/Off Labels setting is in an enabled state.
- [static var isVideoAutoplayEnabled: Bool](uiaccessibility/isvideoautoplayenabled.md)
  A Boolean value that indicates whether the Auto-Play Video Previews setting is in an enabled state.
- [static var buttonShapesEnabled: Bool](uiaccessibility/buttonshapesenabled.md)
  A Boolean value that indicates whether the Button Shapes setting is in an enabled state.
- [static var prefersCrossFadeTransitions: Bool](uiaccessibility/preferscrossfadetransitions.md)
  A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.
- [static var shouldDifferentiateWithoutColor: Bool](uiaccessibility/shoulddifferentiatewithoutcolor.md)
  A Boolean value that indicates whether the Differentiate Without Color setting is in an enabled state.

## See Also

- [Touches, presses, and gestures](touches-presses-and-gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Menus and shortcuts](menus-and-shortcuts.md)
  Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Drag and drop](drag-and-drop.md)
  Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Focus-based navigation](focus-based-navigation.md)
  Navigate the interface of your UIKit app using a remote, game controller, or keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)*