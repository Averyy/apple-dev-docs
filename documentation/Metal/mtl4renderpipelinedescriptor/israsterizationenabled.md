# isRasterizationEnabled

**Framework**: Metal  
**Kind**: property

Determines whether the pipeline rasterizes primitives.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var isRasterizationEnabled: Bool { get set }
```

#### Discussion

By default, this value is [`true`](https://developer.apple.com/documentation/swift/true), specifying that this pipeline rasterizes primitives. Set this property to [`false`](https://developer.apple.com/documentation/swift/false) when you don’t provide a fragment shader function via function [`fragmentFunctionDescriptor`](mtl4renderpipelinedescriptor/fragmentfunctiondescriptor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/israsterizationenabled)*