# MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_:)

**Framework**: Media Accessibility  
**Kind**: func

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

#### Return Value

An array containing the preferred media characteristics for captioning of music, sounds, and dialog. See [`Captions`](captions.md).

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.

## See Also

- [let kMACaptionAppearanceSettingsChangedNotification: CFString](kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](macaptionappearancediddisplaycaptions(_:).md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](macaptionappearancegetdisplaytype(_:).md)
  Returns the preferred type of captions to display.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](macaptionappearancesetdisplaytype(_:_:).md)
  Sets the preference for the type of caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopypreferredcaptioningmediacharacteristics(_:))*