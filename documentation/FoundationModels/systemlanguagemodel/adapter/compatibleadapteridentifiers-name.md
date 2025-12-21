# compatibleAdapterIdentifiers(name:)

**Framework**: Foundation Models  
**Kind**: method

Get all compatible adapter identifiers compatible with current system models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func compatibleAdapterIdentifiers(name: String) -> [String]
```

#### Return Value

All adapter identifiers compatible with current system models, listed in descending order in terms of system preference. You can determine which asset pack or on-demand resource to download with compatible adapter identifiers.

On devices that support Apple Intelligence, the result is guaranteed to be non-empty.

## Parameters

- `name`: Name of the adapter.

## See Also

- [static func isCompatible(AssetPack) -> Bool](systemlanguagemodel/adapter/iscompatible(_:).md)
  Returns a Boolean value that indicates whether an asset pack is an on-device foundation model adapter and is compatible with the system base model version on the runtime device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/compatibleadapteridentifiers(name:))*