# MACaptionAppearanceDisplayType

**Framework**: Media Accessibility  
**Kind**: enum

A value that specifies the type of captions to display.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum MACaptionAppearanceDisplayType
```

## Topics

### Constants
- [MACaptionAppearanceDisplayType.forcedOnly](macaptionappearancedisplaytype/forcedonly.md)
  Do not display captions unless they are forced for translation.
- [MACaptionAppearanceDisplayType.automatic](macaptionappearancedisplaytype/automatic.md)
  If the language of the audio track differs from the system locale, then captions matching the system locale should be displayed (if available). If the language of the audio and the language of the system locale match, no captions are shown.
- [MACaptionAppearanceDisplayType.alwaysOn](macaptionappearancedisplaytype/alwayson.md)
  The most robust available captioning track should always be displayed, whether subtitles, CC, or SDH. This option is selected by a switch labeled “Closed Captions + SDH” (on the Subtitles & Captioning page of iOS) and “Prefer Closed Captions and SDH” checkbox (on the Captions pane of the Accessibility options in macOS).
### Initializers
- [init?(rawValue: CFIndex)](macaptionappearancedisplaytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MACaptionAppearanceDomain](macaptionappearancedomain.md)
  A value that specifies which domain to retrieve a preference setting from.
- [enum MACaptionAppearanceBehavior](macaptionappearancebehavior.md)
  A value that indicates the preferred behavior for a preference setting.
- [enum MACaptionAppearanceFontStyle](macaptionappearancefontstyle.md)
  A value that specifies a font style.
- [enum MACaptionAppearanceTextEdgeStyle](macaptionappearancetextedgestyle.md)
  A value that specifies a style for the outside of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype)*