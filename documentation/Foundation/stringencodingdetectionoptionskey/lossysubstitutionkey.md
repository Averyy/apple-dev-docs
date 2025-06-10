# lossySubstitutionKey

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
static let lossySubstitutionKey: StringEncodingDetectionOptionsKey
```

#### Discussion

Option specifying the string used to substitute for any unsupported characters when converting to a lossy string encoding. If a `@(NO)` value is specified for `NSStringEncodingDetectionAllowLossyKey`, this option has no effect. The corresponding value for this key is an `NSString` object. By default, this value is `U+FFFD`.

## See Also

- [static let allowLossyKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/likelylanguagekey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/lossysubstitutionkey)*