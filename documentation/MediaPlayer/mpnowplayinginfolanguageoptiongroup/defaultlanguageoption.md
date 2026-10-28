# defaultLanguageOption

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The default language option for the group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var defaultLanguageOption: MPNowPlayingInfoLanguageOption? { get }
```

```objc
@property (nonatomic, readonly, nullable) MPNowPlayingInfoLanguageOption * defaultLanguageOption;
```

## Discussion

The value of this property is [`nil`](../../ObjectiveC/nil-227m0.md) when there’s no default language option.

## See Also

### Retrieving language option group information
- [var allowEmptySelection: Bool](./allowemptyselection.md)
  A Boolean that indicates whether the system requires a selection for the language option group.
- [var languageOptions: [MPNowPlayingInfoLanguageOption]](./languageoptions.md)
  The available language options for the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/defaultlanguageoption)*