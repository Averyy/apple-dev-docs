# allowLossyKey

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
static let allowLossyKey: StringEncodingDetectionOptionsKey
```

```c
extern NSStringEncodingDetectionOptionsKey const NSStringEncodingDetectionAllowLossyKey;
```

#### Discussion

Option specifying whether to allow lossy string conversion. The corresponding value for this key is an `NSNumber` object containing a Boolean value. If `@(NO)`, the a lossy string encoding may not be chosen. By default, this value is `@(YES)`.

## See Also

### Type Properties
- [static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey](./disallowedencodingskey.md)
- [static let fromWindowsKey: StringEncodingDetectionOptionsKey](./fromwindowskey.md)
- [static let likelyLanguageKey: StringEncodingDetectionOptionsKey](./likelylanguagekey.md)
- [static let lossySubstitutionKey: StringEncodingDetectionOptionsKey](./lossysubstitutionkey.md)
- [static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey](./suggestedencodingskey.md)
- [static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey](./useonlysuggestedencodingskey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/allowlossykey)*