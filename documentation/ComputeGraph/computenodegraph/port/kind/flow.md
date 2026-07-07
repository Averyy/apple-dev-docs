# ComputeNodeGraph.Port.Kind.flow

**Framework**: Compute Graph  
**Kind**: case

Execution-ordering edge whose destination is conceptually a consumer of the source’s typed output. No runtime payload is transferred, but type compatibility is enforced. Used for stage → stage sequencing.

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
case flow
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/kind/flow)*