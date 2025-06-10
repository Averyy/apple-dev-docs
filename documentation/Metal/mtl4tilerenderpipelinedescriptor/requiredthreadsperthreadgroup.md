# requiredThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property

Sets the required number of threads per threadgroup for tile dispatches.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var requiredThreadsPerThreadgroup: MTLSize { get set }
```

#### Discussion

This value is typically optional, except in the cases where the tile function that [`tileFunctionDescriptor`](mtl4tilerenderpipelinedescriptor/tilefunctiondescriptor.md) references uses `CooperativeTensors`. In this case, you need to provide a non-zero value to this property.

Additionally, when you set this value, the `threadsPerTile` argument of any tile dispatch needs to match it.

Setting this value to a size of 0 in every dimension disables this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4tilerenderpipelinedescriptor/requiredthreadsperthreadgroup)*