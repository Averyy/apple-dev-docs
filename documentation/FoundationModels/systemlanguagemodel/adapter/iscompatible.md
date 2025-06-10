# isCompatible(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns true when an asset pack is an Foundation Models Adapter and compatible with current system base model.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func isCompatible(_ assetPack: AssetPack) -> Bool
```

#### Discussion

This compatibility check is designed to run before downloading the asset pack. It only performs validation on the asset pack name and metadata. `SystemLanguageModel/init(adapterName:)` might still throw errors even if the corresponding asset pack is compatible.

## See Also

- [static func compatibleAdapterIdentifiers(name: String) -> [String]](systemlanguagemodel/adapter/compatibleadapteridentifiers(name:).md)
  Get all compatible adapter identifiers compatible with current system models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/iscompatible(_:))*