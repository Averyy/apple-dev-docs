# addResidencySets:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) addResidencySets:(id<MTLResidencySet> const[]) residencySets count:(NSUInteger) count;
```

## Discussion

Each command queue can maintain a list of up to 32 different residency sets. See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) and [`MTLResidencySet`](../mtlresidencyset.md) for more information.

## Parameters

- `residencySets`: A C array of residency sets, each of which contains resource allocations, such as [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.
- `count`: The number of elements in `residencySets`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/addresidencysets:count:)*