# sharedUniforms

**Framework**: Compute Graph  
**Kind**: property

Uniforms that are shared across multiple graphs, keyed by typeName.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
var sharedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding] { get }
```

#### Discussion

Shared uniforms are stored globally and copied into each simulation’s uniform buffer before GPU execution. Use them for scene-wide values that many simulations read, such as transform matrices, attractors, or colliders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/shareduniforms)*