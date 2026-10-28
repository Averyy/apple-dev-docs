# NSGarbageCollector

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A convenient interface to the garbage collection system.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
@interface NSGarbageCollector : NSObject
```

## Overview

> ❗ **Important**:  Garbage collection is deprecated in OS X 10.8. Use ARC instead—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

Cocoa’s garbage collector is a conservative generational garbage collector. It uses “write-barriers” to detect cross generational stores of pointers so that “young” objects can be collected quickly.

You enable garbage collection (GC) by using the `-fobjc-gc compiler` option. This switch causes the generation of the write-barrier assignment primitives. You must use this option on your main application file *and all others used by the application*, including frameworks and bundles. Bundles are ignored if they are not GC-capable.

The collector determines what is garbage by recursively examining all nodes starting with globals, possible nodes referenced from the thread stacks, and all nodes marked as having “external” references. Nodes not reached by this search are deemed garbage. Weak references to garbage nodes are then cleared.

Garbage nodes that are objects are sent (in an arbitrary order) a [`finalize()`](../ObjectiveC/nsobject-swift.class/finalize%28%29.md) message, and after all `finalize` messages have been sent their memory is recovered. It is a runtime error (referred to as “resurrection”) to store a object being finalized into one that is not. For more details, see Implementing a finalize Method in Garbage Collection Programming Guide.

You can request collection from any thread (see [`collectIfNeeded`](./nsgarbagecollector/collectifneeded.md) and [`collectExhaustively`](./nsgarbagecollector/collectexhaustively.md)).

## Topics

### Shared Instance
- [+ defaultCollector](./nsgarbagecollector/defaultcollector.md)
  Returns the default garbage collector.
### Collection State
- [- disable](./nsgarbagecollector/disable.md)
  Temporarily disables collections.
- [- enable](./nsgarbagecollector/enable.md)
  Enables collection after collection has been disabled.
- [- isEnabled](./nsgarbagecollector/isenabled.md)
  Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process.
- [- isCollecting](./nsgarbagecollector/iscollecting.md)
  Returns a Boolean value that indicates whether a collection is currently in progress.
### Triggering Collection
- [- collectExhaustively](./nsgarbagecollector/collectexhaustively.md)
  Tells the receiver to collect iteratively.
- [- collectIfNeeded](./nsgarbagecollector/collectifneeded.md)
  Tells the receiver to collect if memory consumption thresholds have been exceeded.
### Manipulating External References
- [- disableCollectorForPointer:](./nsgarbagecollector/disablecollectorforpointer_.md)
  Specifies that a given pointer will not be collected.
- [- enableCollectorForPointer:](./nsgarbagecollector/enablecollectorforpointer_.md)
  Specifies that a given pointer may be collected.
### Accessing an Unscanned Memory Zone
- [- zone](./nsgarbagecollector/zone.md)
  Returns a zone of unscanned memory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Legacy
- [NSAllocateCollectable](./nsallocatecollectable.md)
  Allocates collectable memory.
- [NSReallocateCollectable](./nsreallocatecollectable.md)
  Reallocates collectable memory.
- [NSMakeCollectable](./nsmakecollectable.md)
  Makes a newly allocated Core Foundation object eligible for collection.
- [Memory Allocation Options](./api-1539826-memory-allocation-options.md)
  Constants used to control behavior when allocating or reallocating collectible memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector)*