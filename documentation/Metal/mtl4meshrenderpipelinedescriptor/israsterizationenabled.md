# isRasterizationEnabled

**Framework**: Metal  
**Kind**: property

Determines whether the pipeline rasterizes primitives.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isRasterizationEnabled: Bool { get set }
```

#### Discussion

By default, this value is [`true`](https://developer.apple.com/documentation/Swift/true), specifying that this pipeline rasterizes primitives. Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) when you don’t provide a fragment shader function via function [`fragmentFunctionDescriptor`](mtl4meshrenderpipelinedescriptor/fragmentfunctiondescriptor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/israsterizationenabled)*