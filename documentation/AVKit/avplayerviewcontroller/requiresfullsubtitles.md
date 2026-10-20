# requiresFullSubtitles

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether someone can disable the display of subtitles.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var requiresFullSubtitles: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresFullSubtitles;
```

#### Discussion

When this property value is `true`, the subtitle menu doesn’t present the Off or Auto options, because subtitles are always displayed, if available.

The default value is `false`.

## See Also

### Managing subtitles
- [var allowedSubtitleOptionLanguages: [String]?](./allowedsubtitleoptionlanguages.md)
  An array of language codes that restrict the set of subtitle languages available.
- [class var mediaCharacteristicsForSupportedCustomMediaSelectionSchemes: [AVMediaCharacteristic]](./mediacharacteristicsforsupportedcustommediaselectionschemes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresfullsubtitles)*