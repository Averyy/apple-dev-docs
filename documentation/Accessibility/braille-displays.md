# Braille displays

**Framework**: Accessibility

Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.

#### Overview

A refreshable braille display is a hardware device that shows rows of pins that can raise and lower. People who are blind or deafblind use these devices to read digital content through interaction with a screenreader, such as VoiceOver. For information about connecting a braille display to an Apple device, read [`Use a braille display with VoiceOver on iPhone`](https://developer.apple.comhttps://support.apple.com/guide/iphone/use-a-braille-display-iph73b8c43/ios).

A two-dimensional refreshable braille display has a grid of evenly spaced pins that you can use to represent images, charts, and other visual data to VoiceOver users so they can experience your content through touch.

## Topics

### Braille maps
- [class AXBrailleMap](axbraillemap.md)
  A representation of a two-dimensional braille display.
- [protocol AXBrailleMapRenderer](axbraillemaprenderer.md)
  The interface for providing data for a braille map.

## See Also

- [Customized accessibility content](customized-accessibility-content.md)
  Customize your apps to deliver accessibility information to your users in measured portions as they need it.
- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [Hearing device support](hearing-device-support.md)
  Access information about paired hearing aid devices and streaming status.
- [func AXNameFromColor(CGColor) -> String](axnamefromcolor(_:).md)
  Returns a localized description of the color to use in accessibility attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/braille-displays)*