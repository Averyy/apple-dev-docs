# addResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Attaches a residency set to the queue, which Metal attaches to its command buffers as you commit them.

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

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.

## See Also

- [func addResidencySets([any MTLResidencySet])](mtlcommandqueue/addresidencysets(_:).md)
  Attaches multiple residency sets to the queue, which Metal attaches to its command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/addresidencyset(_:))*