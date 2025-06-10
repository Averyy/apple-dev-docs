# motionTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The motion texture this scaler evaluates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var motionTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`motionTextureUsage`](mtlfxtemporaldenoisedscalerbase/motiontextureusage.md) requests and the pixel format that [`motionTextureFormat`](mtlfxtemporaldenoisedscalerdescriptor/motiontextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/motiontexture)*