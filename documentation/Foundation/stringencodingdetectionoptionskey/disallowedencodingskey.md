# disallowedEncodingsKey

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
static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey
```

```c
extern NSStringEncodingDetectionOptionsKey const NSStringEncodingDetectionDisallowedEncodingsKey;
```

#### Discussion

Option specifying any string encodings not to be considered. The corresponding value for this key is an `NSArray` of `NSNumber` objects that contain `NSStringEncoding` values. If this option is unspecified, no additional string encodings are removed from consideration.

## See Also

### Type Properties
- [static let allowLossyKey: StringEncodingDetectionOptionsKey](./allowlossykey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](./likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](./lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](./suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/disallowedencodingskey)*