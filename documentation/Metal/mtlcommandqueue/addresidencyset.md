# addResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addResidencySet(_ residencySet: any MTLResidencySet)
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.

## See Also

- [func addResidencySets([any MTLResidencySet])](mtlcommandqueue/addresidencysets(_:).md)
  Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/addresidencyset(_:))*