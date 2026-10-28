# specularHitDistanceTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The specular hit texture this scaler evaluates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var specularHitDistanceTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> specularHitDistanceTexture;
```

## Discussion

You are responsible for ensuring the usage and pixel format of the texture you assign to this property matches the texture usage [`specularHitDistanceTextureUsage`](./specularhitdistancetextureusage.md) requests and the pixel format that [`specularHitDistanceTextureFormat`](../mtlfxtemporaldenoisedscalerdescriptor/specularhitdistancetextureformat.md) requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase/specularhitdistancetexture)*