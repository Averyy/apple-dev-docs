# zone

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a zone of unscanned memory.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (NSZone *) zone;
```

#### Return Value

A memory zone of memory that is not scanned.

#### Discussion

The collector provides a [`NSZoneMalloc`](../nszonemalloc.md)-style allocation interface, primarily for compatibility with existing code that maintains zone affinity. Such memory is unscanned and you must free it using [`NSZoneFree`](../nszonefree.md).  This is exactly equivalent to calling [`NSAllocateCollectable`](../nsallocatecollectable.md) with the option [`NSCollectorDisabledOption`](../nscollectordisabledoption.md).

You should typically allocate garbage-collected memory using [`NSAllocateCollectable`](../nsallocatecollectable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/zone)*