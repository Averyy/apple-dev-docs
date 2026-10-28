# NSGrayColorSpaceModel

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The grayscale color-space model.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`NSColorSpace.Model.gray`](./nscolorspace/model/gray.md) instead.

## Declaration

```c
static const NSColorSpaceModel NSGrayColorSpaceModel;
```

## Discussion

Can refer to both device-dependent and generic color space variants.

## See Also

### Deprecated constants
- [NSUnknownColorSpaceModel](./nsunknowncolorspacemodel.md)
  An unknown color-space model.
- [NSRGBColorSpaceModel](./nsrgbcolorspacemodel.md)
  The RGB (red green blue) color-space model.
- [NSCMYKColorSpaceModel](./nscmykcolorspacemodel.md)
  The CYMK (cyan, yellow, magenta, black) color-space model.
- [NSLABColorSpaceModel](./nslabcolorspacemodel.md)
  The L*a*b* device-independent color-space model, which represents colors relative to a reference white point.
- [NSDeviceNColorSpaceModel](./nsdevicencolorspacemodel.md)
  DeviceN is a color-space model from Adobe Systems, Inc. used in PostScript and PDF color specification.
- [NSIndexedColorSpaceModel](./nsindexedcolorspacemodel.md)
  An indexed color space, which identifies specified discrete colors in a color list by index number. An indexed color value (a color specification in indexed color space) consists of an index value that refers to a color in a color list.
- [NSPatternColorSpaceModel](./nspatterncolorspacemodel.md)
  Identifies a pattern color space, which is simply an image that is repeated over and over again in a tiled pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraycolorspacemodel)*