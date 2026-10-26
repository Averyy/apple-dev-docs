# localizedAssetPacks

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The subset of asset packs in this manifest that best match the current preferred languages.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (copy, readonly) NSSet<BAAssetPack *> * localizedAssetPacks;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## See Also

### Getting localized asset packs
- [- localizedAssetPacksForLanguage:](./localizedassetpacksforlanguage_.md)
  Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/localizedassetpacks)*