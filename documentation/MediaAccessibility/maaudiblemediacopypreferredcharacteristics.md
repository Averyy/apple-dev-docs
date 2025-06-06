# MAAudibleMediaCopyPreferredCharacteristics()

**Framework**: Media Accessibility  
**Kind**: func

Returns the preference for audible media characteristics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray>
```

## See Also

- [let kMAAudibleMediaSettingsChangedNotification: CFString](kmaaudiblemediasettingschangednotification.md)
  A notification that occurs when any user-defined audible media settings change.
- [let MAMediaCharacteristicDescribesVideoForAccessibility: CFString](mamediacharacteristicdescribesvideoforaccessibility.md)
  A media characteristic that indicates that a track or media selection option includes audible content that describes a video for accessibility.
- [let MAMediaCharacteristicDescribesMusicAndSoundForAccessibility: CFString](mamediacharacteristicdescribesmusicandsoundforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that describes music and sound other than spoken dialog.
- [let MAMediaCharacteristicTranscribesSpokenDialogForAccessibility: CFString](mamediacharacteristictranscribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that transcribes spoken dialog and identifies the speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maaudiblemediacopypreferredcharacteristics())*