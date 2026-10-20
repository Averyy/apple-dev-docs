# MACaptionAppearanceGetDisplayType(_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the preferred type of captions to display.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceGetDisplayType(_ domain: MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType
```

```c
extern MACaptionAppearanceDisplayType MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain domain);
```

#### Return Value

A value representing options to use only forced captions, allow system locale to override the language of the audio track, or choose the best available captioning track from CC, SDH, or subtitles. See [`MACaptionAppearanceDisplayType`](./macaptionappearancedisplaytype.md).

## Parameters

- `domain`: The domain to retrieve the preference value from. See [`MACaptionAppearanceDomain`](./macaptionappearancedomain.md). Pass [`MACaptionAppearanceDomain.user`](./macaptionappearancedomain/user.md) unless the system defaults are needed for comparison.

## See Also

### General settings
- [let kMACaptionAppearanceSettingsChangedNotification: CFString](./kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](./macaptionappearancediddisplaycaptions%28_%29.md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](./macaptionappearancecopypreferredcaptioningmediacharacteristics%28_%29.md)
  Returns the preferences for captioning sounds.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](./macaptionappearancesetdisplaytype%28_,_%29.md)
  Sets the preference for the type of caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancegetdisplaytype(_:))*