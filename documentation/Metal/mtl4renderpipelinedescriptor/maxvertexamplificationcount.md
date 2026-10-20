# maxVertexAmplificationCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Determines the maximum value that can you can pass as the pipeline’s amplification count.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maxVertexAmplificationCount: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger maxVertexAmplificationCount;
```

#### Discussion

This property controls the maximum count you pass to [`setVertexAmplificationCount:viewMappings:`](../mtl4rendercommandencoder/setvertexamplificationcount_viewmappings_.md) when using vertex amplification with this pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/maxvertexamplificationcount)*