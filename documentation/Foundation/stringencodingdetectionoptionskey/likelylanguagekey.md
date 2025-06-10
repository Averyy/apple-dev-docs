# likelyLanguageKey

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Option specifying the likely two-letter ISO 639-1 language code for the converted string. Use this when you have prior knowledge about the expected language of the converted string. The corresponding value for this key is an `NSString` object. If no value is specified, the language of the converted string is not considered.

## See Also

- [static let allowLossyKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/fromwindowskey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/likelylanguagekey)*