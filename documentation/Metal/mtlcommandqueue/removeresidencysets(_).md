# removeResidencySets(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS

## Declaration

```swift
func removeResidencySets(_ residencySets: [any MTLResidencySet])
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

The method doesn’t remove the residency sets from command buffers the queue owns with a [`status`](../mtlcommandbuffer/status.md) property that’s equal to [`MTLCommandBufferStatus.committed`](../mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](../mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: An array of residency sets, each of which contains resource allocations, such as [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.

## See Also

### Detaching residency sets
- [func removeResidencySet(any MTLResidencySet)](./removeresidencyset%28_%29.md)
  Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencysets(_:))*