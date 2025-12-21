# fragmentFunctionDescriptor

**Framework**: Metal  
**Kind**: property

Assigns the shader function that this pipeline executes for each fragment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var fragmentFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

#### Discussion

When you don’t specify a fragment function, you need to disable rasterization by setting property [`isRasterizationEnabled`](mtl4renderpipelinedescriptor/israsterizationenabled.md) to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/fragmentfunctiondescriptor)*