# mediaCharacteristicsForSupportedCustomMediaSelectionSchemes

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+

## Declaration

```swift
class var mediaCharacteristicsForSupportedCustomMediaSelectionSchemes: [AVMediaCharacteristic] { get }
```

```objc
@property (class, readonly) NSArray<NSString *> * mediaCharacteristicsForSupportedCustomMediaSelectionSchemes;
```

## Discussion

Returns available AVKit supported media group types.

## See Also

### Managing subtitles
- [var allowedSubtitleOptionLanguages: [String]?](./allowedsubtitleoptionlanguages.md)
  An array of language codes that restrict the set of subtitle languages available.
- [var requiresFullSubtitles: Bool](./requiresfullsubtitles.md)
  A Boolean value that indicates whether someone can disable the display of subtitles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/mediacharacteristicsforsupportedcustommediaselectionschemes)*