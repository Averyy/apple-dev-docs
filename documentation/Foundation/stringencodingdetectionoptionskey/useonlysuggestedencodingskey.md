# useOnlySuggestedEncodingsKey

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
static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey
```

#### Discussion

Option specifying whether to only consider suggested string encodings. Use this only if you specify a value for `NSStringEncodingDetectionSuggestedEncodingsKey`. The corresponding value for this key is an `NSNumber` object containing a Boolean value. By default, this value is `@(NO)`.

## See Also

- [static let allowLossyKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/suggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/useonlysuggestedencodingskey)*