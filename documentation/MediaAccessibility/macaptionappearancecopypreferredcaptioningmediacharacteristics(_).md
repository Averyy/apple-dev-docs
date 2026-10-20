# MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the preferences for captioning sounds.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray>
```

```c
extern CFArrayRefMACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain domain);
```

#### Return Value

An array containing the preferred media characteristics for captioning of music, sounds, and dialog. See [Captions](./captions.md).

## Parameters

- `domain`: The domain to retrieve the preference value from. See [`MACaptionAppearanceDomain`](./macaptionappearancedomain.md). Pass [`MACaptionAppearanceDomain.user`](./macaptionappearancedomain/user.md) unless the system defaults are needed for comparison.

## See Also

### General settings
- [let kMACaptionAppearanceSettingsChangedNotification: CFString](./kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](./macaptionappearancediddisplaycaptions%28_%29.md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](./macaptionappearancegetdisplaytype%28_%29.md)
  Returns the preferred type of captions to display.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](./macaptionappearancesetdisplaytype%28_,_%29.md)
  Sets the preference for the type of caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopypreferredcaptioningmediacharacteristics(_:))*