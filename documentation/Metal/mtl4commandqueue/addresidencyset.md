# addResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func addResidencySet(_ residencySet: any MTLResidencySet)
```

#### Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/addresidencyset(_:))*