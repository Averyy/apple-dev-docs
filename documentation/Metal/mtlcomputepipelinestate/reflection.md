# reflection

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Provides access to this compute pipeline’s reflection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var reflection: MTLComputePipelineReflection? { get }
```

#### Discussion

Reflection is `nil` if you create the pipeline state object directly from the [`MTLDevice`](mtldevice.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/reflection)*