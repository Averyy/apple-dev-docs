# fromWindowsKey

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
static let fromWindowsKey: StringEncodingDetectionOptionsKey
```

#### Discussion

Option specifying whether to consider string encodings corresponding to Windows codepage numbers. The corresponding value for this key is an `NSNumber` object containing a Boolean value. If `@(YES)`, Windows string encodings are removed from consideration. By default, this value is `@(NO)`.

## See Also

- [static let allowLossyKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey/useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/fromwindowskey)*