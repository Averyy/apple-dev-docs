# pipelineIndependent

**Framework**: Metal  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var pipelineIndependent: MTLFunctionOptions { get }
```

#### Discussion

All pipeline states. The function needs to be linked to the pipeline that will use this function. This function option can only be used for functions that are compiled with `MTLFunctionOptionCompileToBinary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions/pipelineindependent)*