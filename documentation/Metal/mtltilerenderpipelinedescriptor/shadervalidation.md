# shaderValidation

**Framework**: Metal  
**Kind**: property

A value that enables or disables shader validation for the pipeline.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var shaderValidation: MTLShaderValidation { get set }
```

#### Discussion

You can override the value using either of these environment variables: `MTL_SHADER_VALIDATION_ENABLE_PIPELINES` or `MTL_SHADER_VALIDATION_DISABLE_PIPELINES.`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/shadervalidation)*