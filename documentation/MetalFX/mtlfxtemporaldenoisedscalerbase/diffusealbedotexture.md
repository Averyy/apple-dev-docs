# diffuseAlbedoTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The diffuse albedo texture this scaler evaluates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var diffuseAlbedoTexture: (any MTLTexture)? { get set }
```

#### Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`diffuseAlbedoTextureUsage`](mtlfxtemporaldenoisedscalerbase/diffusealbedotextureusage.md) requests and the pixel format that [`diffuseAlbedoTextureFormat`](mtlfxtemporaldenoisedscalerdescriptor/diffusealbedotextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/diffusealbedotexture)*