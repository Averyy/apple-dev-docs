# useResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Applies a residency set to a command buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func useResidencySet(_ residencySet: any MTLResidencySet)
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.

## See Also

- [func useResidencySets([any MTLResidencySet])](mtlcommandbuffer/useresidencysets(_:).md)
  Applies multiple residency sets to a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencyset(_:))*