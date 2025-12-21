# reflection

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Provides access to this compute pipeline’s reflection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var reflection: MTLComputePipelineReflection? { get }
```

#### Discussion

Reflection is `nil` if you create the pipeline state object directly from the [`MTLDevice`](mtldevice.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/reflection)*