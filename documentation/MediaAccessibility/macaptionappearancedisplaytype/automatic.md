# MACaptionAppearanceDisplayType.automatic

**Framework**: Media Accessibility  
**Kind**: case

If the language of the audio track differs from the system locale, then captions matching the system locale should be displayed (if available). If the language of the audio and the language of the system locale match, no captions are shown.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

## See Also

- [MACaptionAppearanceDisplayType.forcedOnly](macaptionappearancedisplaytype/forcedonly.md)
  Do not display captions unless they are forced for translation.
- [MACaptionAppearanceDisplayType.alwaysOn](macaptionappearancedisplaytype/alwayson.md)
  The most robust available captioning track should always be displayed, whether subtitles, CC, or SDH. This option is selected by a switch labeled “Closed Captions + SDH” (on the Subtitles & Captioning page of iOS) and “Prefer Closed Captions and SDH” checkbox (on the Captions pane of the Accessibility options in macOS).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/automatic)*