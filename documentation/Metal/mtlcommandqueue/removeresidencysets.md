# removeResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Detaches multiple residency sets from the command queue, which prevents Metal from attaching them to the queue’s command buffers as you commit them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+

## Declaration

```swift
func removeResidencySets(_ residencySets: [any MTLResidencySet])
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

The method doesn’t remove the residency sets from command buffers the queue owns with a [`status`](mtlcommandbuffer/status.md) property that’s equal to [`MTLCommandBufferStatus.committed`](mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md).

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as  ,  , and   instances.

## See Also

- [func removeResidencySet(any MTLResidencySet)](mtlcommandqueue/removeresidencyset(_:).md)
  Detaches a residency set from the command queue, which prevents Metal from attaching it to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencysets(_:))*