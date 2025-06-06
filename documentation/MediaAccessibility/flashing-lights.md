# Flashing lights

**Framework**: Media Accessibility

Detect, mitigate, and inform people about flashing lights in media content.

#### Overview

People might want to avoid bright, frequent flashes of light in the media they consume. The Dim Flashing Lights setting allows the system to calculate, mitigate, and inform people about flashing lights in a piece of media.

In your app, respond to changes in the Dim Flashing Lights setting to create an enjoyable media-viewing experience for people who choose to reduce flashing lights on their devices. To respond to changes in this setting, register for the notification [`kMADimFlashingLightsChangedNotification`](kmadimflashinglightschangednotification.md).

```swift
import MediaAccessibility

NotificationCenter.default.addObserver(self,     
    selector: #selector(dimFlashingLightsChanged),     
    name: kMADimFlashingLightsChangedNotification as NSNotification.Name,     
    object: nil)
```

When the Dim Flashing Lights setting changes, update your UI accordingly. For example, when a person enables this setting on the device:

- If you have a custom media-timeline viewer, update the timeline viewer to indicate the strength of the flashing lights in the media content.
- If you have separate media assets for content without flashing lights, play the content without flashing lights and inform the viewer when the content starts.
- If you have an animation sequence with flashing lights in a game or app that you can control programmatically, adjust the animation accordingly.

Check the value of the Dim Flashing Lights setting at any time by using [`MADimFlashingLightsEnabled()`](madimflashinglightsenabled().md).

```swift
@objc 
func dimFlashingLightsChanged(_ notification: Notification) {
    if MADimFlashingLightsEnabled() {
        // Play media without flashing lights and inform the viewer.
    } else {
        // Play standard media.
    }
}
```

## Topics

### Dim flashing lights
- [Responding to changes in the flashing lights setting](responding-to-changes-in-the-flashing-lights-setting.md)
  Adjust your UI when a person chooses to dim flashing lights on their Apple device.
- [func MADimFlashingLightsEnabled() -> Bool](madimflashinglightsenabled().md)
  Returns a Boolean value that indicates whether the flashing lights setting is enabled on the device.
- [let kMADimFlashingLightsChangedNotification: CFString](kmadimflashinglightschangednotification.md)
  A notification that posts when a person changes the flashing lights setting on the device.
- [class MAFlashingLightsProcessor](maflashinglightsprocessor.md)
  A class that processes a framebuffer object to detect and dim sequences of flashing lights.

## See Also

- [Captions](captions.md)
  Coordinate the presentation of closed-captioned data for your app’s media files.
- [Music Haptics](music-haptics.md)
  Play haptic tracks along with known music tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/flashing-lights)*