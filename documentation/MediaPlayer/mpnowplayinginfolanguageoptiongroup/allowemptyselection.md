# allowEmptySelection

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the system requires a selection for the language option group.

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
var allowEmptySelection: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL allowEmptySelection;
```

#### Discussion

When set to [`true`](../../Swift/true.md), there must be a language option in the language option group.

## See Also

### Retrieving language option group information
- [var defaultLanguageOption: MPNowPlayingInfoLanguageOption?](./defaultlanguageoption.md)
  The default language option for the group.
- [var languageOptions: [MPNowPlayingInfoLanguageOption]](./languageoptions.md)
  The available language options for the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/allowemptyselection)*