# addResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+

## Declaration

```swift
func addResidencySets(_ residencySets: [any MTLResidencySet])
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as  ,  , and   instances.

## See Also

- [func addResidencySet(any MTLResidencySet)](mtlcommandqueue/addresidencyset(_:).md)
  Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/addresidencysets(_:))*