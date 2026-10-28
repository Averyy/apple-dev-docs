# likelyLanguageKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let likelyLanguageKey: StringEncodingDetectionOptionsKey
```

```c
extern NSStringEncodingDetectionOptionsKey const NSStringEncodingDetectionLikelyLanguageKey;
```

## Discussion

Option specifying the likely two-letter ISO 639-1 language code for the converted string. Use this when you have prior knowledge about the expected language of the converted string. The corresponding value for this key is an `NSString` object. If no value is specified, the language of the converted string is not considered.

## See Also

### Type Properties
- [static let allowLossyKey: StringEncodingDetectionOptionsKey](./allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](./disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./fromwindowskey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](./lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](./suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/likelylanguagekey)*