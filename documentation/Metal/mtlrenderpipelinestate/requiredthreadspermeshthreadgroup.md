# requiredThreadsPerMeshThreadgroup

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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
var requiredThreadsPerMeshThreadgroup: MTLSize { get }
```

```objc
@property (readonly) MTLSize requiredThreadsPerMeshThreadgroup;
```

#### Discussion

The required size of every mesh shader threadgroup.

This value is set in MTLMeshRenderPipelineDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/requiredthreadspermeshthreadgroup)*