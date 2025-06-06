# removeResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Detaches a residency set from the command queue, which prevents Metal from attaching it to the queue’s command buffers as you commit them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func removeResidencySet(_ residencySet: any MTLResidencySet)
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

The method doesn’t remove the residency set from command buffers the queue owns with a [`status`](mtlcommandbuffer/status.md) property that’s equal to [`MTLCommandBufferStatus.committed`](mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md).

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.

## See Also

- [func removeResidencySets([any MTLResidencySet])](mtlcommandqueue/removeresidencysets(_:).md)
  Detaches multiple residency sets from the command queue, which prevents Metal from attaching them to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencyset(_:))*