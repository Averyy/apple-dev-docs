# UIAccessibility

**Framework**: UIKit

A set of methods that provides accessibility information about views and controls in an app’s user interface.

#### Overview

The `UIAccessibility` informal protocol provides accessibility information about an app’s user interface elements. Assistive apps, such as VoiceOver, convey this information to users with disabilities to help them use the app.

Standard UIKit controls and views implement the `UIAccessibility` methods and are accessible to assistive apps by default. This means that if your app uses only standard controls and views, such as [`UIButton`](uibutton.md), [`UISegmentedControl`](uisegmentedcontrol.md), and [`UITableView`](uitableview.md), you need only supply app-specific details when the default values are incomplete. You can do this by setting these values in Interface Builder or by setting the properties in this informal protocol.

The [`UIAccessibilityElement`](uiaccessibilityelement.md) class, which represents custom user interface objects, also implements the `UIAccessibility` informal protocol. If you create a completely custom [`UIView`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) subclass, you might need to create an instance of [`UIAccessibilityElement`](uiaccessibilityelement.md) to represent it. In this case, you’d support all the `UIAccessibility` properties to correctly set and return the accessibility element’s properties.

## Topics

### Supporting basic accessibility
- [var isAccessibilityElement: Bool](../objectivec/nsobject-swift.class/isaccessibilityelement.md)
- [var accessibilityLabel: String?](../objectivec/nsobject-swift.class/accessibilitylabel.md)
- [var accessibilityValue: String?](../objectivec/nsobject-swift.class/accessibilityvalue.md)
- [var accessibilityHint: String?](../objectivec/nsobject-swift.class/accessibilityhint.md)
- [var accessibilityTraits: UIAccessibilityTraits](../objectivec/nsobject-swift.class/accessibilitytraits.md)
- [struct UIAccessibilityTraits](uiaccessibilitytraits.md)
  Constants that describe how an accessibility element behaves.
### Defining accessibility text and language
- [Speech attributes for attributed strings](speech-attributes-for-attributed-strings.md)
  Apply attributes to text in an attributed string to modify the pronunciation of that text.
- [Text attributes for attributed strings](text-attributes-for-attributed-strings.md)
  Apply attributes to text in an attributed string to convey extra information about the text.
- [var accessibilityHeaderElements: [Any]?](../objectivec/nsobject-swift.class/accessibilityheaderelements.md)
- [var accessibilityAttributedHint: NSAttributedString?](../objectivec/nsobject-swift.class/accessibilityattributedhint.md)
- [var accessibilityAttributedLabel: NSAttributedString?](../objectivec/nsobject-swift.class/accessibilityattributedlabel.md)
- [var accessibilityLanguage: String?](../objectivec/nsobject-swift.class/accessibilitylanguage.md)
- [var accessibilityTextualContext: UIAccessibilityTextualContext?](../objectivec/nsobject-swift.class/accessibilitytextualcontext.md)
- [var accessibilityUserInputLabels: [String]!](../objectivec/nsobject-swift.class/accessibilityuserinputlabels.md)
- [var accessibilityAttributedUserInputLabels: [NSAttributedString]!](../objectivec/nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [var accessibilityAttributedValue: NSAttributedString?](../objectivec/nsobject-swift.class/accessibilityattributedvalue.md)
### Configuring behavior
- [var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?](../objectivec/nsobject-swift.class/accessibilitycustomrotors.md)
- [var accessibilityElementsHidden: Bool](../objectivec/nsobject-swift.class/accessibilityelementshidden.md)
- [var accessibilityRespondsToUserInteraction: Bool](../objectivec/nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [var accessibilityViewIsModal: Bool](../objectivec/nsobject-swift.class/accessibilityviewismodal.md)
- [var shouldGroupAccessibilityChildren: Bool](../objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren.md)
- [var accessibilityDirectTouchOptions: UIAccessibility.DirectTouchOptions](../objectivec/nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [UIAccessibility.DirectTouchOptions](uiaccessibility/directtouchoptions.md)
  Constants that configure how VoiceOver produces audio for direct touch areas.
### Handling notifications
- [Notification names](notification-names.md)
  The names of notifications that the accessibility system generates.
- [Notification dictionary keys](notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.
- [UIAccessibility.Notification](uiaccessibility/notification.md)
  An accessibility notification that an app can send.
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](uiaccessibility/post(notification:argument:).md)
  Posts a notification to assistive apps.
### Navigating elements
- [UIAccessibilityContainer](uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [var accessibilityActivationPoint: CGPoint](../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [var accessibilityFocusedUIElement: Any?](../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [var accessibilityFrame: CGRect](../objectivec/nsobject-swift.class/accessibilityframe.md)
- [func accessibilityHitTest(NSPoint) -> Any?](../objectivec/nsobject-swift.class/accessibilityhittest(_:).md)
- [var accessibilityNavigationStyle: UIAccessibilityNavigationStyle](../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [enum UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md)
  Constants that describe how to navigate an object’s elements with an assistive app.
- [var accessibilityPath: UIBezierPath?](../objectivec/nsobject-swift.class/accessibilitypath.md)
- [static func zoomFocusChanged(zoomType: UIAccessibility.ZoomType, toFrame: CGRect, in: UIView)](uiaccessibility/zoomfocuschanged(zoomtype:toframe:in:).md)
  Notifies the system when the app’s focus changes to a new location.
- [UIAccessibility.ZoomType](uiaccessibility/zoomtype.md)
  The types of system Zoom that can be in effect.
- [static var assistiveTouch: UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature/assistivetouch.md)
  The AssistiveTouch accessibility feature.
### Supporting types
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
- [typealias AXTraitsReturnBlock](axtraitsreturnblock.md)
- [typealias AXUITextInputReturnBlock](axuitextinputreturnblock.md)
- [typealias AXVoidReturnBlock](axvoidreturnblock.md)
- [struct UIAccessibility](uiaccessibility.md)
  A namespace for accessibility symbols for UIKit apps.

## See Also

- [Accessibility](../accessibility/accessibility.md)
  Make your apps accessible to everyone who uses Apple devices.
- [Accessibility for UIKit](accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.
- [UIAccessibilityContainer](uiaccessibilitycontainer.md)
  Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md)
  Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility-protocol)*