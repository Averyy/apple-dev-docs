# namedUniforms

**Framework**: Compute Graph  
**Kind**: property

Uniforms that are named and exposed as parameters of this graph, keyed by name.

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
var namedUniforms: [String : ComputeNodeGraph.Assembly.UniformBinding] { get }
```

#### Discussion

Unlike [`sharedUniforms`](computenodegraph/assembly/shareduniforms.md), named uniforms are local to this graph and not shared with other graphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/nameduniforms)*