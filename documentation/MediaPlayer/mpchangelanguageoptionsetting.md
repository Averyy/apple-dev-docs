# MPChangeLanguageOptionSetting

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

The states that determine when language option changes take effect.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MPChangeLanguageOptionSetting
```

```c
enum MPChangeLanguageOptionSetting : NSInteger;
```

## Topics

### Enumeration Cases
- [MPChangeLanguageOptionSetting.none](./mpchangelanguageoptionsetting/none.md)
  No language option change is to be made.
- [MPChangeLanguageOptionSetting.nowPlayingItemOnly](./mpchangelanguageoptionsetting/nowplayingitemonly.md)
  The language option change is applied to the now playing item only.
- [MPChangeLanguageOptionSetting.permanent](./mpchangelanguageoptionsetting/permanent.md)
  The language option change is applied to all future playback items.
### Initializers
- [init?(rawValue: Int)](./mpchangelanguageoptionsetting/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Changing the language option
- [var languageOption: MPNowPlayingInfoLanguageOption](./mpchangelanguageoptioncommandevent/languageoption.md)
  The requested language option to change.
- [var setting: MPChangeLanguageOptionSetting](./mpchangelanguageoptioncommandevent/setting.md)
  The extent of the language setting change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting)*