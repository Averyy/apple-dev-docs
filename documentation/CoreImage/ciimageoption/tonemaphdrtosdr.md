# toneMapHDRtoSDR

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 14.1+
- iPadOS 14.1+
- Mac Catalyst 14.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let toneMapHDRtoSDR: CIImageOption
```

```c
extern CIImageOption const kCIImageToneMapHDRtoSDR;
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
- [static let providerTileSize: CIImageOption](./providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
- [static let providerUserInfo: CIImageOption](./provideruserinfo.md)
  A key for data needed by the image provider. The associated value is an object that contains the needed data.
- [static let textureFormat: CIImageOption](./textureformat.md)
  The key for an OpenGL texture format.
- [static let textureTarget: CIImageOption](./texturetarget.md)
  The key for an OpenGL texture target.
- [static let contentHeadroom: CIImageOption](./contentheadroom.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/tonemaphdrtosdr)*