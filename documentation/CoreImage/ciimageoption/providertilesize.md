# providerTileSize

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let providerTileSize: CIImageOption
```

```c
extern CIImageOption const kCIImageProviderTileSize;
```

## See Also

### Type Properties
- [static let applyOrientationProperty: CIImageOption](./applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let cacheImmediately: CIImageOption](./cacheimmediately.md)
- [static let colorSpace: CIImageOption](./colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](./expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](./nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](./properties.md)
  The key for image metadata properties.
- [static let providerUserInfo: CIImageOption](./provideruserinfo.md)
  A key for data needed by the image provider. The associated value is an object that contains the needed data.
- [static let textureFormat: CIImageOption](./textureformat.md)
  The key for an OpenGL texture format.
- [static let textureTarget: CIImageOption](./texturetarget.md)
  The key for an OpenGL texture target.
- [static let toneMapHDRtoSDR: CIImageOption](./tonemaphdrtosdr.md)
- [static let contentHeadroom: CIImageOption](./contentheadroom.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/providertilesize)*