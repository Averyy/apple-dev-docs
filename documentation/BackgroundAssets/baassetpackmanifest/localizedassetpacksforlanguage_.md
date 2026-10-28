# localizedAssetPacksForLanguage:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns the subset of asset packs in this manifest that are available to download and that best match the specified language.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (NSSet<BAAssetPack *> *) localizedAssetPacksForLanguage:(NSString *) languageIdentifier;
```

## Return Value

The localized asset packs.

## Discussion

Depending on which languages are available, the returned asset packs’ respective languages may not exactly match the specified language.

## Parameters

- `languageIdentifier`: The language’s BCP-47 identifier.

## See Also

### Getting localized asset packs
- [localizedAssetPacks](./localizedassetpacks.md)
  The subset of asset packs in this manifest that best match the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/localizedassetpacksforlanguage:)*