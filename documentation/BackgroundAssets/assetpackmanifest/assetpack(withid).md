# assetPack(withID:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns the asset pack in this manifest with the given ID.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func assetPack(withID id: String) -> AssetPack?
```

## Return Value

The asset pack, if it could be found in this manifest; otherwise, `nil`.

## Parameters

- `id`: The asset pack’s ID.

## See Also

### Getting asset packs
- [let assetPacks: Set<AssetPack>](./assetpacks.md)
  The asset packs in this manifest that are available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/assetpack(withid:))*