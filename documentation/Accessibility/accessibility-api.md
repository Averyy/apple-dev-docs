# Accessibility API

**Framework**: Accessibility

Browse API in the Accessibility framework.

#### Overview

While many Apple frameworks provide built-in accessibility support, the Accessibility framework defines API for supporting additional accessibility features across multiple platforms. The Accessibility framework includes API that enable you to:

- Respond to changes in Accessibility system settings
- Post accessibility notifications
- Define an accessible representation of your chart to support audio graphs
- Interact with hardware such as braille displays and hearing devices
- Generate a localized description of a color

## Topics

### System settings
- [struct AccessibilitySettings](accessibilitysettings.md)
  A structure for working with accessibility system settings.
### Notifications
- [enum AccessibilityNotification](accessibilitynotification.md)
  Types of accessibility notifications that an app can post.
### Assistive technologies
- [struct AccessibilityTechnology](accessibilitytechnology.md)
- [static let automation: AccessibilityTechnology](accessibilitytechnology/automation.md)
- [static let fullKeyboardAccess: AccessibilityTechnology](accessibilitytechnology/fullkeyboardaccess.md)
- [static let hoverText: AccessibilityTechnology](accessibilitytechnology/hovertext.md)
- [static let speakScreen: AccessibilityTechnology](accessibilitytechnology/speakscreen.md)
- [static let switchControl: AccessibilityTechnology](accessibilitytechnology/switchcontrol.md)
- [static let voiceControl: AccessibilityTechnology](accessibilitytechnology/voicecontrol.md)
- [static let voiceOver: AccessibilityTechnology](accessibilitytechnology/voiceover.md)
- [static let zoom: AccessibilityTechnology](accessibilitytechnology/zoom.md)
- [class AccessibilityRequest](accessibilityrequest.md)
### Features
- [Customized accessibility content](customized-accessibility-content.md)
  Customize your apps to deliver accessibility information to your users in measured portions as they need it.
- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [Hearing device support](hearing-device-support.md)
  Access information about paired hearing aid devices and streaming status.
- [func AXNameFromColor(CGColor) -> String](axnamefromcolor(_:).md)
  Returns a localized description of the color to use in accessibility attributes.
### Braille
- [Braille displays](braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [class AXBrailleTable](axbrailletable.md)
  A rule for translating print text to Braille, and back-translating Braille to print text.
- [class AXBrailleTranslator](axbrailletranslator.md)
  Translates print text to Braille and Braille to print text according to the given Braille table.
- [class AXBrailleTranslationResult](axbrailletranslationresult.md)
  The result of translation or back-translation.
### Math expressions
- [class AXMathExpressionNumber](axmathexpressionnumber.md)
- [class AXMathExpressionIdentifier](axmathexpressionidentifier.md)
- [class AXMathExpressionOperator](axmathexpressionoperator.md)
- [class AXMathExpressionText](axmathexpressiontext.md)
- [class AXMathExpressionFenced](axmathexpressionfenced.md)
- [class AXMathExpressionRow](axmathexpressionrow.md)
- [class AXMathExpressionTable](axmathexpressiontable.md)
- [class AXMathExpressionTableCell](axmathexpressiontablecell.md)
- [class AXMathExpressionTableRow](axmathexpressiontablerow.md)
- [class AXMathExpressionUnderOver](axmathexpressionunderover.md)
- [class AXMathExpressionSubSuperscript](axmathexpressionsubsuperscript.md)
- [class AXMathExpressionFraction](axmathexpressionfraction.md)
- [class AXMathExpressionMultiscript](axmathexpressionmultiscript.md)
- [class AXMathExpressionRoot](axmathexpressionroot.md)
- [class AXMathExpression](axmathexpression.md)
- [protocol AXMathExpressionProvider](axmathexpressionprovider.md)
### Override sessions
- [class AXFeatureOverrideSession](axfeatureoverridesession.md)
  A token object that represents an override session held by your app.
- [class AXFeatureOverrideSessionManager](axfeatureoverridesessionmanager.md)
  A manager class to begin and end accessibility feature override sessions. Multiple override sessions are reconciled by combining the requests, preferring feature enablement. Ending all sessions restores the prior state of Accessibility feature enablement. Your app must be entitled with com.apple.developer.accessibility.merchant-api-control.
- [AXFeatureOverrideSession.Options](axfeatureoverridesession/options.md)
  Options indicating which Accessibility features will be turned on or off when an override session is held by your app.
- [let AXFeatureOverrideSessionErrorDomain: String](axfeatureoverridesessionerrordomain.md)
- [struct AXFeatureOverrideSessionError](axfeatureoverridesessionerror-swift.struct.md)
- [AXFeatureOverrideSessionError.Code](axfeatureoverridesessionerror-swift.struct/code.md)
- [com.apple.developer.accessibility.merchant-api-control](../BundleResources/Entitlements/com.apple.developer.accessibility.merchant-api-control.md)
### Deprecated
- [func AXAnimatedImagesEnabled() -> Bool](axanimatedimagesenabled().md)
  Returns a Boolean value that indicates whether the system setting for Animated Images is on.
- [func AXPrefersHeadAnchorAlternative() -> Bool](axprefersheadanchoralternative().md)
  Returns a Boolean value that indicates the person’s preference for content that follows their head position.
- [func AXPrefersHorizontalTextLayout() -> Bool](axprefershorizontaltextlayout().md)
  Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibility-api)*