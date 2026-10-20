# kMAAudibleMediaSettingsChangedNotification

**Framework**: Media Accessibility  
**Kind**: var  
**Role**: Global Variable

A notification that occurs when any user-defined audible media settings change.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let kMAAudibleMediaSettingsChangedNotification: CFString
```

```c
extern CFStringRef const kMAAudibleMediaSettingsChangedNotification;
```

## See Also

### Audible media selection settings
- [func MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray>](./maaudiblemediacopypreferredcharacteristics%28%29.md)
  Returns the preference for audible media characteristics.
- [let MAMediaCharacteristicDescribesVideoForAccessibility: CFString](./mamediacharacteristicdescribesvideoforaccessibility.md)
  A media characteristic that indicates that a track or media selection option includes audible content that describes a video for accessibility.
- [let MAMediaCharacteristicDescribesMusicAndSoundForAccessibility: CFString](./mamediacharacteristicdescribesmusicandsoundforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that describes music and sound other than spoken dialog.
- [let MAMediaCharacteristicTranscribesSpokenDialogForAccessibility: CFString](./mamediacharacteristictranscribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that transcribes spoken dialog and identifies the speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/kmaaudiblemediasettingschangednotification)*