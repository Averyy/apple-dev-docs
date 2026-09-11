# localizedAssetPacks

**Framework**: Background Assets  
**Kind**: property

The subset of asset packs in this manifest that best match the current preferred languages.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var localizedAssetPacks: Set<AssetPack> { get }
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

## See Also

- [func localizedAssetPacks(for: Locale.Language) -> Set<AssetPack>](assetpackmanifest/localizedassetpacks(for:).md)
  Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/localizedassetpacks)*