# useResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Applies multiple residency sets to a command buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+

## Declaration

```swift
func useResidencySets(_ residencySets: [any MTLResidencySet])
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as  ,  , and   instances.

## See Also

- [func useResidencySet(any MTLResidencySet)](mtlcommandbuffer/useresidencyset(_:).md)
  Applies a residency set to a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencysets(_:))*