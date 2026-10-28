# useResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) useResidencySet:(id<MTLResidencySet>) residencySet;
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

## Discussion

Each command buffer can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](../mtlresidencyset.md) for more information.

## Parameters

- `residencySet`: A residency set that contains resource allocations, such as [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.

## See Also

### Attaching residency sets
- [func useResidencySets([any MTLResidencySet])](./useresidencysets%28_%29.md)
  Applies multiple residency sets to a command buffer.
- [- useResidencySets:count:](./useresidencysets_count_.md)
  Applies multiple residency sets to a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/useresidencyset(_:))*