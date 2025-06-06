# heap

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The heap on which the resource is allocated, if any.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var heap: (any MTLHeap)? { get }
```

#### Discussion

This value is `nil` if the resource isn’t allocated on a heap.

## See Also

- [var heapOffset: Int](mtlresource/heapoffset.md)
  The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [func makeAliasable()](mtlresource/makealiasable.md)
  Allows future heap resource allocations to alias against the resource’s memory, reusing it.
- [func isAliasable() -> Bool](mtlresource/isaliasable.md)
  A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/heap)*