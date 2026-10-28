# suggestedEncodingsKey

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
static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey
```

```c
extern NSStringEncodingDetectionOptionsKey const NSStringEncodingDetectionSuggestedEncodingsKey;
```

## Discussion

Option specifying any suggested string encodings. Use this when you have prior knowledge about the likely or expected encoding. The corresponding value for this key is an `NSArray` of `NSNumber` objects that contain `NSStringEncoding` values. If this option is unspecified, all allowed encodings are evaluated with equal consideration.

## See Also

### Type Properties
- [static let allowLossyKey: StringEncodingDetectionOptionsKey](./allowlossykey.md)
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](./disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](./likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](./lossysubstitutionkey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/suggestedencodingskey)*