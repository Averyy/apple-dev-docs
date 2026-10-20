# MACaptionAppearanceDomain

**Framework**: Media Accessibility  
**Kind**: enum  
**Role**: Enumeration

A value that specifies which domain to retrieve a preference setting from.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum MACaptionAppearanceDomain
```

```c
enum MACaptionAppearanceDomain : CFIndex;
```

## Topics

### Constants
- [MACaptionAppearanceDomain.default](./macaptionappearancedomain/default.md)
  The system default value for the setting should be returned.
- [MACaptionAppearanceDomain.user](./macaptionappearancedomain/user.md)
  The user’s preferred value for the setting should be returned.
### Enumeration Cases
- [MACaptionAppearanceDomain.videoConferencing](./macaptionappearancedomain/videoconferencing.md)
### Initializers
- [init?(rawValue: CFIndex)](./macaptionappearancedomain/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum MACaptionAppearanceDisplayType](./macaptionappearancedisplaytype.md)
  A value that specifies the type of captions to display.
- [enum MACaptionAppearanceBehavior](./macaptionappearancebehavior.md)
  A value that indicates the preferred behavior for a preference setting.
- [enum MACaptionAppearanceFontStyle](./macaptionappearancefontstyle.md)
  A value that specifies a font style.
- [enum MACaptionAppearanceTextEdgeStyle](./macaptionappearancetextedgestyle.md)
  A value that specifies a style for the outside of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain)*