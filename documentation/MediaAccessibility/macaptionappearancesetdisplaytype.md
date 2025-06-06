# MACaptionAppearanceSetDisplayType(_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Sets the preference for the type of caption.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceSetDisplayType(_ domain: MACaptionAppearanceDomain, _ displayType: MACaptionAppearanceDisplayType)
```

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.
- `displayType`: A value representing options to use only forced captions, to allow system locale to override the language of the audio track, or to choose the best available captioning track from CC, SDH, or subtitles. See  .

## See Also

- [let kMACaptionAppearanceSettingsChangedNotification: CFString](kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](macaptionappearancediddisplaycaptions(_:).md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopypreferredcaptioningmediacharacteristics(_:).md)
  Returns the preferences for captioning sounds.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](macaptionappearancegetdisplaytype(_:).md)
  Returns the preferred type of captions to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancesetdisplaytype(_:_:))*