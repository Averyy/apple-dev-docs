# MACaptionAppearanceBehavior

**Framework**: Media Accessibility  
**Kind**: enum

A value that indicates the preferred behavior for a preference setting.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum MACaptionAppearanceBehavior
```

## Topics

### Constants
- [MACaptionAppearanceBehavior.useValue](macaptionappearancebehavior/usevalue.md)
  The preference setting should always be used.
- [MACaptionAppearanceBehavior.useContentIfAvailable](macaptionappearancebehavior/usecontentifavailable.md)
  The preference setting should be used unless the content media being played has its own custom value for this setting.
### Initializers
- [init?(rawValue: CFIndex)](macaptionappearancebehavior/init(rawvalue:).md)

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
- [enum MACaptionAppearanceDisplayType](macaptionappearancedisplaytype.md)
  A value that specifies the type of captions to display.
- [enum MACaptionAppearanceFontStyle](macaptionappearancefontstyle.md)
  A value that specifies a font style.
- [enum MACaptionAppearanceTextEdgeStyle](macaptionappearancetextedgestyle.md)
  A value that specifies a style for the outside of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior)*