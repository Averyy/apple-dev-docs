# Customized accessibility content

**Framework**: Accessibility

Customize your apps to deliver accessibility information to your users in measured portions as they need it.

#### Overview

The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.

For example, in a photography app, you may want the user to know the date, time, orientation, and shutter speed for a photo. However, the user might not always need that complete set of information. Using the custom content provider in your app lets the user experience the content in way that’s more appropriate for an assistive technology.

## Topics

### Custom accessibility content
- [class AXCustomContent](axcustomcontent.md)
  Objects that define custom content and the timing of its output.
- [protocol AXCustomContentProvider](axcustomcontentprovider.md)
  The interface for customizing the accessibility content.
- [typealias AXCustomContentReturnBlock](axcustomcontentreturnblock.md)

## See Also

- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [Hearing device support](hearing-device-support.md)
  Access information about paired hearing aid devices and streaming status.
- [func AXNameFromColor(CGColor) -> String](axnamefromcolor(_:).md)
  Returns a localized description of the color to use in accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/customized-accessibility-content)*