# isCompatible(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean value that indicates whether an asset pack is an on-device foundation model adapter and is compatible with the system base model version on the runtime device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func isCompatible(_ assetPack: AssetPack) -> Bool
```

#### Discussion

Use this check when choosing an adapter asset pack to download. This check only validates the asset pack name and metadata, so initializing the adapter with [`init(name:)`](systemlanguagemodel/adapter/init(name:).md) — or loading the adapter onto the base model with [`init(adapter:guardrails:)`](systemlanguagemodel/init(adapter:guardrails:).md) — may throw errors if the adapter has a compatibility issue despite having correct metadata.

> **Note**: Run this check before you download an adapter asset pack to confirm if it’s usable on the runtime device.

## See Also

- [static func compatibleAdapterIdentifiers(name: String) -> [String]](systemlanguagemodel/adapter/compatibleadapteridentifiers(name:).md)
  Get all compatible adapter identifiers compatible with current system models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/iscompatible(_:))*