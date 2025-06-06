# Memory Allocation Options

**Framework**: Foundation

Constants used to control behavior when allocating or reallocating collectible memory.

#### Overview

These constants are used as components in a bitfield to specify the behavior of [`NSAllocateCollectable`](nsallocatecollectable.md) and [`NSReallocateCollectable`](nsreallocatecollectable.md).

## Topics

### Constants
- [var NSScannedOption: Int](nsscannedoption.md)
  Specifies allocation of scanned memory.
- [var NSCollectorDisabledOption: Int](nscollectordisabledoption.md)
  Specifies that the block is retained, and therefore ineligible for collection. Specifying this option is equivalent to invoking [`disableCollectorForPointer:`](nsgarbagecollector/disablecollectorforpointer:.md) with the returned block as the argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1539826-memory-allocation-options)*