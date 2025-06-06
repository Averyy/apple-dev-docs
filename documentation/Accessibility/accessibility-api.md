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
- [Braille displays](braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [Hearing device support](hearing-device-support.md)
  Access information about paired hearing aid devices and streaming status.
- [func AXNameFromColor(CGColor) -> String](axnamefromcolor(_:).md)
  Returns a localized description of the color to use in accessibility attributes.
### Deprecated
- [func AXAnimatedImagesEnabled() -> Bool](axanimatedimagesenabled().md)
  Returns a Boolean value that indicates whether the system setting for Animated Images is on.
- [func AXPrefersHeadAnchorAlternative() -> Bool](axprefersheadanchoralternative().md)
  Returns a Boolean value that indicates the person’s preference for content that follows their head position.
- [func AXPrefersHorizontalTextLayout() -> Bool](axprefershorizontaltextlayout().md)
  Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibility-api)*