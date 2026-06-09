# localizedAssetPacks(for:)

**Framework**: Background Assets  
**Kind**: method

Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func localizedAssetPacks(for language: Locale.Language) -> Set<AssetPack>
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Return Value

The localized asset packs.

#### Discussion

Depending on which languages are available, the returned asset packs’ respective languages may not exactly match the specified language.

## Parameters

- `language`: The language.

## See Also

- [var localizedAssetPacks: Set<AssetPack>](assetpackmanifest/localizedassetpacks.md)
  The subset of asset packs in this manifest that best match the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/localizedassetpacks(for:))*