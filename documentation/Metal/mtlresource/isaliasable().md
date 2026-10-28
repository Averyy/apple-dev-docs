# isAliasable()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) isAliasable;
```

## Return Value

The default value is [`false`](../../Swift/false.md). The value is [`true`](../../Swift/true.md) only if the [`makeAliasable()`](./makealiasable%28%29.md) method was previously called on this resource.

## See Also

### Managing heap resources
- [var heapOffset: Int](./heapoffset.md)
  The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [var heap: (any MTLHeap)?](./heap.md)
  The heap on which the resource is allocated, if any.
- [func makeAliasable()](./makealiasable%28%29.md)
  Allows future heap resource allocations to alias against the resource’s memory, reusing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource/isaliasable())*