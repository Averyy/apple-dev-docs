# templateItems

**Framework**: AVFoundation  
**Kind**: property

An array of player item configurations to use as templates for player items that play interstitial content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var templateItems: [AVPlayerItem] { get set }
```

#### Discussion

If you require the system to create new player items using the same asset instance as the template item, create the asset with an [`AVURLAssetPrimarySessionIdentifierKey`](avurlassetprimarysessionidentifierkey.md) value equal to [`httpSessionIdentifier`](avurlasset/httpsessionidentifier.md) of the primary item’s [`asset`](avplayeritem/asset.md). Creating assets this way simplifies cases where you require loading their data with a custom [`AVAssetResourceLoader`](avassetresourceloader.md) delegate.

> ❗ **Important**:  The system raises an exception if template items contain assets that aren’t URL based, such as [`AVComposition`](avcomposition.md).

 The system raises an exception if template items contain assets that aren’t URL based, such as [`AVComposition`](avcomposition.md).

## See Also

- [var primaryItem: AVPlayerItem?](avplayerinterstitialevent/primaryitem.md)
  The player item that represents the primary content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/templateitems)*