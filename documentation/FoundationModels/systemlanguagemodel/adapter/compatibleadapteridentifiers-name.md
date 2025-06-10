# compatibleAdapterIdentifiers(name:)

**Framework**: Foundation Models  
**Kind**: method

Get all compatible adapter identifiers compatible with current system models.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func compatibleAdapterIdentifiers(name: String) -> [String]
```

#### Return Value

All adapter identifiers compatible with current system models, listed in descending order in terms of system preference. You can determine which asset pack or on-demand resource to download with compatible adapter identifiers.

On devices that support Apple Intelligence, the result is guaranteed to be non-empty.

## See Also

- [static func isCompatible(AssetPack) -> Bool](systemlanguagemodel/adapter/iscompatible(_:).md)
  Returns true when an asset pack is an Foundation Models Adapter and compatible with current system base model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/compatibleadapteridentifiers(name:))*