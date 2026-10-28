# externalSubtitleOptionLanguages

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- tvOS 9.0+ - Deprecated in 9.0

## Declaration

```objc
@property (nonatomic, copy) NSArray<NSString *> * externalSubtitleOptionLanguages;
```

## Discussion

An array of BCP 47 language codes that supplements the list of subtitle options that will be presented to the user.

This list is strictly for non-standard, application-rendered subtitles, that cannot be handled by AVFoundation. Most clients should not need to set this property. The application should implement the playerViewController:didSelectExternalSubtitleOptionLanguage: method of its AVPlayerViewControllerDelegate to be notified when one of these languages has been chosen by the user.

## See Also

### Setting subtitle options
- [selectedExternalSubtitleOptionLanguage](./selectedexternalsubtitleoptionlanguage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/externalsubtitleoptionlanguages)*