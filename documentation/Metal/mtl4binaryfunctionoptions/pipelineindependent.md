# pipelineIndependent

**Framework**: Metal  
**Kind**: property

Compiles the function to have its function handles return a constant MTLResourceID across all pipeline states. The function needs to be linked to the pipeline that will use this function.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var pipelineIndependent: MTL4BinaryFunctionOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4binaryfunctionoptions/pipelineindependent)*