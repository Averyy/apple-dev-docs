# removeResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func removeResidencySet(_ residencySet: any MTLResidencySet)
```

#### Discussion

The method doesn’t remove the residency set from command buffers the queue owns with an [`status`](mtlcommandbuffer/status.md) property that’s equal to [`MTLCommandBufferStatus.committed`](mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md).

See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as  ,  , and   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/removeresidencyset(_:))*