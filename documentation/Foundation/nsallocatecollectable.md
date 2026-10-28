# NSAllocateCollectable

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Allocates collectable memory.

**Availability**:
- macOS 10.0+

> **Deprecated**: Garbage collection is deprecated in OS X v10.8; instead,you should use AutomaticReference Counting—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

## Declaration

```c
extern void *NSAllocateCollectable(NSUInteger size, NSUInteger options);
```

## Return Value

A pointer to the allocated memory, or `NULL` if the function is unable to allocate the requested memory.

## Parameters

- `size`: The number of bytes of memory to allocate.
- `options`: `0` or `NSScannedOption`: A value of `0` allocates non-scanned memory; a value of `NSScannedOption` allocates scanned memory.

## See Also

### Legacy
- [NSGarbageCollector](./nsgarbagecollector.md)
  A convenient interface to the garbage collection system.
- [NSReallocateCollectable](./nsreallocatecollectable.md)
  Reallocates collectable memory.
- [NSMakeCollectable](./nsmakecollectable.md)
  Makes a newly allocated Core Foundation object eligible for collection.
- [Memory Allocation Options](./api-1539826-memory-allocation-options.md)
  Constants used to control behavior when allocating or reallocating collectible memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsallocatecollectable)*