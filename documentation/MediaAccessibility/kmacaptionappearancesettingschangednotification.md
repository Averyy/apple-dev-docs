# kMACaptionAppearanceSettingsChangedNotification

**Framework**: Media Accessibility  
**Kind**: var

A notification that occurs when any user-defined caption settings change.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let kMACaptionAppearanceSettingsChangedNotification: CFString
```

## See Also

- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](macaptionappearancediddisplaycaptions(_:).md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopypreferredcaptioningmediacharacteristics(_:).md)
  Returns the preferences for captioning sounds.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](macaptionappearancegetdisplaytype(_:).md)
  Returns the preferred type of captions to display.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](macaptionappearancesetdisplaytype(_:_:).md)
  Sets the preference for the type of caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/kmacaptionappearancesettingschangednotification)*