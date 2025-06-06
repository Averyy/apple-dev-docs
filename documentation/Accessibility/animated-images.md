# Animated images

**Framework**: Accessibility

Pause animations in animated images in your app when people turn off the Animated Images setting.

#### Overview

People use the Animated Images setting to control whether to play animated images like GIFs on the web and in apps. By default, the setting is on, which allows animated images to play automatically. A person can turn off the setting to indicate that they want to pause animated images on their device.

In your app, handle changes to the Animated Images setting to create an enjoyable experience for people who choose to pause animated images. Register for the notification [`animatedImagesEnabledDidChangeNotification`](accessibilitysettings/animatedimagesenableddidchangenotification.md) to respond to changes in this setting:

```swift
import Accessibility

NotificationCenter.default.addObserver(self,
    selector: #selector(animatedImagesChanged),
    name: NSNotification.Name.animatedImagesEnabledDidChangeNotification,
    object: nil)
```

When the Animated Images setting changes, perform changes to your UI to pause animated images:

```swift
@objc 
func animatedImagesChanged(_ notification: Notification) {
    if AccessibilitySettings.animatedImagesEnabled {
        // The setting is on. Animate images.
    } else {
        // The setting is off. Pause animations in animated images.
    }
}
```

Check the value of the Animated Images setting at any time by using [`animatedImagesEnabled`](accessibilitysettings/animatedimagesenabled.md).

## Topics

### Animated images
- [static var animatedImagesEnabled: Bool](accessibilitysettings/animatedimagesenabled.md)
  A Boolean value that indicates whether the system setting for playing animated images is on.
- [static var animatedImagesEnabledDidChangeNotification: Notification.Name](accessibilitysettings/animatedimagesenableddidchangenotification.md)
  A notification that posts when the system setting for playing animated images changes.

## See Also

- [VoiceOver](voiceover.md)
  A gesture-based screen reader that provides an auditory description of the content onscreen.
- [Flashing lights](../MediaAccessibility/flashing-lights.md)
  Detect, mitigate, and inform people about flashing lights in media content.
- [Audio graphs](audio-graphs.md)
  Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [Braille displays](braille-displays.md)
  Display a graphical representation of images, icons, data, and more on a two-dimensional braille display.
- [Horizontal text](horizontal-text.md)
  Lay out vertical text horizontally in your app when people turn on the Prefer Horizontal Text setting.
- [WWDC21 Challenge: Large Text Challenge](wwdc21_challenge_large_text_challenge.md)
  Design for large text sizes by modifying the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/animated-images)*