# layer(url:type:)

**Framework**: DiskImageKit  
**Kind**: method  
**Role**: Type Method

Creates a configuration object for a new Apple sparse image format (ASIF) disk image layer.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static func layer(url: URL, type: DiskImage.LayerType) -> ASIFLayerCreationConfiguration
```

#### Return Value

An [`ASIFLayerCreationConfiguration`](../asiflayercreationconfiguration.md) that you can use` for stacking operations.

#### Discussion

Use this factory method to create a configuration that can be used with [`appending(_:)`](../diskimage/appending%28_%29-3pfqg.md). Use the configuration this method returns only for appending to stacked images, not for standalone image creation.

For more information on ASIF layer creation for stacked images, see [`asifLayer(url:type:)`](../diskimage/creationconfiguration/asiflayer%28url,type%29.md) .

## Parameters

- `url`: The [`URL`](../../Foundation/url.md) for a file that’s the backing store of the image.
- `type`: The [`DiskImage.LayerType`](../diskimage/layertype-swift.struct.md) of the layer to create (a cache or overlay layer with an optional block count).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/asifcreationconfiguration/layer(url:type:))*