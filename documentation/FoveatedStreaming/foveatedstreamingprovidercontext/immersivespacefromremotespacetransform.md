# immersiveSpaceFromRemoteSpaceTransform

**Framework**: Foveated Streaming  
**Kind**: property

Transform matrix from the remote space to the immersive space.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var immersiveSpaceFromRemoteSpaceTransform: simd_float4x4 { get }
```

#### Discussion

This matrix is used to align the streamed content with the person’s physical space. The host app may update this value during the session via [`immersiveSpaceFromRemoteSpaceTransform`](foveatedstreamingsession/immersivespacefromremotespacetransform.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/immersivespacefromremotespacetransform)*