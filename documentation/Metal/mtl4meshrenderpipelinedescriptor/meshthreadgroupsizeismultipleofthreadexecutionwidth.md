# meshThreadgroupSizeIsMultipleOfThreadExecutionWidth

**Framework**: Metal  
**Kind**: property

Provides a guarantee to Metal regarding the number of threadgroup threads for the mesh stage of a pipeline you create from this descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var meshThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool { get set }
```

#### Discussion

If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true), you state to Metal that when you use a mesh render pipeline you create from this descriptor, the number of threadgroup threads you dispatch for the mesh stage is a multiple of its [`meshThreadExecutionWidth`](mtlrenderpipelinestate/meshthreadexecutionwidth.md). The compiler’s optimizer can use this guarantee to generate more efficient code.

This property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth)*