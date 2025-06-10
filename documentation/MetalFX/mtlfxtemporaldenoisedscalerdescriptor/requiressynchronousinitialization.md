# requiresSynchronousInitialization

**Framework**: MetalFX  
**Kind**: property

A Boolean value that indicates whether MetalFX compiles a temporal scaling effect’s underlying upscaler as it creates the instance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
var requiresSynchronousInitialization: Bool { get set }
```

#### Discussion

This property gives you the option to decide when it’s better for your app to give MetalFX the time it needs to compile the underlying upscaler of the temporal scaling effect. The two choices are:

- As you create the effect
- After you create the effect, likely when your app needs to upscale the initial textures

You can create a temporal denoised scaler instance that can denoise and upscale textures at its best speed immediately after you create it by setting this property to [`true`](https://developer.apple.com/documentation/swift/true) and then calling an initialization method like [`newTemporalDenoisedScaler(with:)`](mtlfxtemporaldenoisedscalerdescriptor/newtemporaldenoisedscaler(with:).md). However, it may take MetalFX more time for that method to return while it creates the denoiser scaler and compiles its underlying pipelines.

By default, the property is equal to [`false`](https://developer.apple.com/documentation/swift/false), which tells MetalFX to quickly create and return the temporal scaling-effect instance, and then compile a faster upscaler in the background. However, this means the effect can take more time to upscale textures while the framework compiles the underlying upscaler. When the framework finishes compiling, the effect runs just as fast as if you set the property to [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**: The image quality of the effect’s output texture is consistent, whether it’s using the slower interim upscaler or the final, faster upscaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/requiressynchronousinitialization)*