# selectedExternalSubtitleOptionLanguage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- tvOS 9.0+ - Deprecated in 9.0

## Declaration

```objc
@property (nonatomic, copy) NSString * selectedExternalSubtitleOptionLanguage;
```

## Discussion

Specifies BCP 47 language code of the external subtitle option language marked in the user interface.

If anything other than an external subtitle option is selected (including “Off”), then this property should be set to an empty string. If the value is not an empty string, it should be an element of the externalSubtitleOptionLanguages array.

## See Also

### Setting subtitle options
- [externalSubtitleOptionLanguages](./externalsubtitleoptionlanguages.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedexternalsubtitleoptionlanguage)*