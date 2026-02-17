# reflection

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var reflection: MTLRenderPipelineReflection? { get }
```

#### Discussion

> 💡 **Tip**:  Verify the apps that need reflection information in production by testing them without a frame capture, Metal API validation layer, or shader validation layer.

The property is `nil` when you create a pipeline state from an[`MTLDevice`](mtldevice.md) instance, such as with its [`makeRenderPipelineState(descriptor:)`](mtldevice/makerenderpipelinestate(descriptor:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/reflection)*