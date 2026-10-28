# lossySubstitutionKey

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
static let lossySubstitutionKey: StringEncodingDetectionOptionsKey
```

```c
extern NSStringEncodingDetectionOptionsKey const NSStringEncodingDetectionLossySubstitutionKey;
```

## Discussion

Option specifying the string used to substitute for any unsupported characters when converting to a lossy string encoding. If a `@(NO)` value is specified for `NSStringEncodingDetectionAllowLossyKey`, this option has no effect. The corresponding value for this key is an `NSString` object. By default, this value is `U+FFFD`.

## See Also

### Type Properties
- [static let allowLossyKey: StringEncodingDetectionOptionsKey](./allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](./disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](./likelylanguagekey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](./suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/lossysubstitutionkey)*