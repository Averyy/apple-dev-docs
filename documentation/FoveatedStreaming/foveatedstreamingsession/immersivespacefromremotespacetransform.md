# immersiveSpaceFromRemoteSpaceTransform

**Framework**: Foveated Streaming  
**Kind**: property

A transform matrix which maps from the streamed scene’s coordinate space origin to the origin of the app’s immersive space.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var immersiveSpaceFromRemoteSpaceTransform: simd_float4x4 { get set }
```

#### Discussion

By default, the origin of the remote scene matches the origin of your app’s immersive space. You can use this API to manipulate that conversion – e.g. to travel around a larger scene.

For example, the following moves the entire streamed scene 5 meters to the right along the X axis:

```swift
    session.immersiveSpaceFromRemoteSpaceTransform = Transform(translation: [5, 0, 0]).matrix
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivespacefromremotespacetransform)*