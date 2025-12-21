# isAliasable()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func isAliasable() -> Bool
```

#### Return Value

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). The value is [`true`](https://developer.apple.com/documentation/Swift/true) only if the [`makeAliasable()`](mtlresource/makealiasable().md) method was previously called on this resource.

## See Also

- [var heapOffset: Int](mtlresource/heapoffset.md)
  The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [var heap: (any MTLHeap)?](mtlresource/heap.md)
  The heap on which the resource is allocated, if any.
- [func makeAliasable()](mtlresource/makealiasable.md)
  Allows future heap resource allocations to alias against the resource’s memory, reusing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/isaliasable())*