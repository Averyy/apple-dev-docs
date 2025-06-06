# Horizontal text

**Framework**: Accessibility

Lay out vertical text horizontally in your app when people turn on the Prefer Horizontal Text setting.

#### Overview

People use the Prefer Horizontal Text setting to specify a preference for laying out text horizontally in languages that support vertical text. By default, the setting is off, which allows languages that support vertical text to lay out text vertically. A person can turn on the setting to indicate that they prefer a horizontal text layout where possible.

In your app, handle changes to the Prefer Horizontal Text setting to create an enjoyable experience for people who choose to opt in to a horizontal text layout. Register for the notification [`prefersHorizontalTextLayoutDidChangeNotification`](accessibilitysettings/prefershorizontaltextlayoutdidchangenotification.md) to respond to changes in this setting:

```swift
import Accessibility

NotificationCenter.default.addObserver(self,
    selector: #selector(prefersHorizontalTextChanged),
    name: NSNotification.Name.prefersHorizontalTextLayoutDidChangeNotification,
    object: nil)
```

When the Prefer Horizontal Text setting changes, perform changes to your UI to update how you lay out text:

```swift
@objc 
func prefersHorizontalTextChanged(_ notification: Notification) {
    if AccessibilitySettings.prefersHorizontalTextLayout {
        // The setting is on. Use a horizontal layout for text where possible.
    } else {
        // The setting is off. Use a vertical layout for languages that support vertical text.
    }
}
```

Check the value of the Prefer Horizontal Text setting at any time by using [`prefersHorizontalTextLayout`](accessibilitysettings/prefershorizontaltextlayout.md).

## Topics

### Horizontal text
- [static var prefersHorizontalTextLayout: Bool](accessibilitysettings/prefershorizontaltextlayout.md)
  A Boolean value that indicates whether the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout is on.
- [static var prefersHorizontalTextLayoutDidChangeNotification: Notification.Name](accessibilitysettings/prefershorizontaltextlayoutdidchangenotification.md)
  A notification that posts when the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout changes.

## See Also

- [VoiceOver](voiceover.md)
  A gesture-based screen reader that provides an auditory description of the content onscreen.
- [Flashing lights](../MediaAccessibility/flashing-lights.md)
  Detect, mitigate, and inform people about flashing lights in media content.
- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [Braille displays](braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [Animated images](animated-images.md)
  Pause animations in animated images in your app when people turn off the Animated Images setting.
- [WWDC21 Challenge: Large Text Challenge](wwdc21_challenge_large_text_challenge.md)
  Design for large text sizes by modifying the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/horizontal-text)*