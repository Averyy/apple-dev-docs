# immersiveSpaceFromRemoteSceneTransform

**Framework**: Foveated Streaming  
**Kind**: property  
**Required**: Yes

Transform matrix from the remote scene’s coordinate space to the immersive space.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
var immersiveSpaceFromRemoteSceneTransform: simd_float4x4 { get set }
```

#### Discussion

This matrix is used to align the streamed content with the user’s physical space. The host app may update this value during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/delegate/immersivespacefromremotescenetransform)*