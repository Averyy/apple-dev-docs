# languageOptions

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The available language options for the group.

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
var languageOptions: [MPNowPlayingInfoLanguageOption] { get }
```

```objc
@property (nonatomic, readonly) NSArray<MPNowPlayingInfoLanguageOption *> * languageOptions;
```

#### Discussion

This property contains an array of available language options for the group.

## See Also

### Retrieving language option group information
- [var allowEmptySelection: Bool](./allowemptyselection.md)
  A Boolean that indicates whether the system requires a selection for the language option group.
- [var defaultLanguageOption: MPNowPlayingInfoLanguageOption?](./defaultlanguageoption.md)
  The default language option for the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/languageoptions)*