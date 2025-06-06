# MACaptionAppearanceDidDisplayCaptions(_:)

**Framework**: Media Accessibility  
**Kind**: func

Informs accessibility clients when captions display onscreen.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceDidDisplayCaptions(_ strings: CFArray)
```

## See Also

- [let kMACaptionAppearanceSettingsChangedNotification: CFString](kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopypreferredcaptioningmediacharacteristics(_:).md)
  Returns the preferences for captioning sounds.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](macaptionappearancegetdisplaytype(_:).md)
  Returns the preferred type of captions to display.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](macaptionappearancesetdisplaytype(_:_:).md)
  Sets the preference for the type of caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancediddisplaycaptions(_:))*