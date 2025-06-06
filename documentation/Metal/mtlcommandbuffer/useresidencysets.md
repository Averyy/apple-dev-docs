# useResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Attaches multiple residency sets to the command buffer.

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

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as  ,  , and   instances.

## See Also

- [func useResidencySet(any MTLResidencySet)](mtlcommandbuffer/useresidencyset(_:).md)
  Attaches a residency set to the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencysets(_:))*