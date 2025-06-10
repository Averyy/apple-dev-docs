# reflection

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

Obtains a reflection object for this render pipeline.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var reflection: MTLRenderPipelineReflection? { get }
```

#### Discussion

When you create the pipeline through an [`MTLDevice`](mtldevice.md) instance, reflection is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/reflection)*