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

> **Note**: ![Graph](/images/com.apple.computegraph/viewpoint.svg)

> **Note**: Reads from shared uniform Viewpoint


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/viewpoint-swift.func)*