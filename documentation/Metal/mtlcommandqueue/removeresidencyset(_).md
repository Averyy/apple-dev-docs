# removeResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.

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

```objc
- (void) removeResidencySet:(id<MTLResidencySet>) residencySet;
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

The method doesn’t remove the residency set from command buffers the queue owns with a [`status`](../mtlcommandbuffer/status.md) property that’s equal to [`MTLCommandBufferStatus.committed`](../mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](../mtlcommandbufferstatus/scheduled.md).

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](../mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.

## See Also

### Detaching residency sets
- [func removeResidencySets([any MTLResidencySet])](./removeresidencysets%28_%29.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
- [- removeResidencySets:count:](./removeresidencysets_count_.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/removeresidencyset(_:))*