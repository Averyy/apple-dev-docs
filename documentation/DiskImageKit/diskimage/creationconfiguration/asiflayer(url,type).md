# asifLayer(url:type:)

**Framework**: DiskImageKit  
**Kind**: method  
**Role**: Type Method

Returns an Apple sparse image format (ASIF) configuration for stackable layers.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static func asifLayer(url: URL, type: DiskImage.LayerType) -> Self
```

Available when `Self` is `ASIFLayerCreationConfiguration`.

## Return Value

An [`ASIFLayerCreationConfiguration`](../../asiflayercreationconfiguration.md) instance for stacking use.

## Discussion

The following example demonstrates how to append a new cache layer to a base image:

```
var stackedImage = try baseImage.appending(.asifLayer(url: cacheURL, type: .cache))
```

## Parameters

- `url`: The [`URL`](../../../Foundation/url.md) for the disk image file.
- `type`: The type of layer (cache or overlay).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/creationconfiguration/asiflayer(url:type:))*