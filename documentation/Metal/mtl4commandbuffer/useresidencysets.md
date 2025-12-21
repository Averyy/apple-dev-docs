# useResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Applies multiple residency sets to a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func useResidencySets(_ residencySets: [any MTLResidencySet])
```

#### Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as  ,  , and   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/useresidencysets(_:))*