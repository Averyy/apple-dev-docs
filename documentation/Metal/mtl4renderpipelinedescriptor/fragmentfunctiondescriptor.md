# fragmentFunctionDescriptor

**Framework**: Metal  
**Kind**: property

Assigns the shader function that this pipeline executes for each fragment.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var fragmentFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

#### Discussion

When you don’t specify a fragment function, you need to disable rasterization by setting property [`isRasterizationEnabled`](mtl4renderpipelinedescriptor/israsterizationenabled.md) to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/fragmentfunctiondescriptor)*