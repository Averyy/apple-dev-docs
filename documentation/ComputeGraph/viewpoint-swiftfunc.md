# viewpoint

**Framework**: Compute Graph  
**Kind**: func

Returns the current viewpoint, if one is provided.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
Viewpoint viewpoint()
```

#### Discussion

Depending on context, this may include direction, position, or both values. On visionOS, a `ParticleViewpoint` component needs to be added to the scene to automatically provide this value.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/cdd7d98ff4f620e378ad4026a7f938c8/viewpoint.svg)

> **Note**: Reads from shared uniform Viewpoint


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/viewpoint-swift.func)*