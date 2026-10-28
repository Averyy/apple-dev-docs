# heapOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var heapOffset: Int { get }
```

```objc
@property (readonly) NSUInteger heapOffset;
```

## Discussion

If the heap is not a placement heap ([`MTLHeapType.placement`](../mtlheaptype/placement.md)), the value is always `0` and should be ignored.

## See Also

### Managing heap resources
- [var heap: (any MTLHeap)?](./heap.md)
  The heap on which the resource is allocated, if any.
- [func makeAliasable()](./makealiasable%28%29.md)
  Allows future heap resource allocations to alias against the resource’s memory, reusing it.
- [func isAliasable() -> Bool](./isaliasable%28%29.md)
  A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/heapoffset)*