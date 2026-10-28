# NSPointerFunctions.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Defines the memory and personality options for an `NSPointerFunctions` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Options
```

```c
enum NSPointerFunctionsOptions : NSUInteger;
```

## Overview

When specifying a value, you can use only one of the options listed in Memory Options,  only one of the options listed in Personality Options, and any number of other options.

## Topics

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](./options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](./options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](./options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](./options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](./options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [var NSMapTableStrongMemory: NSPointerFunctions.Options](../nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](./options/strongmemory.md).
- [var NSMapTableWeakMemory: NSPointerFunctions.Options](../nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](./options/weakmemory.md).
- [NSPointerFunctionsZeroingWeakMemory](../nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md)
  Use weak read and write barriers; use garbage-collected memory on copyIn.
- [NSMapTableZeroingWeakMemory](../nsmaptablezeroingweakmemory.md)
  Equivalent to [`NSPointerFunctionsZeroingWeakMemory`](../nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).
### Personality Options
- [static var cStringPersonality: NSPointerFunctions.Options](./options/cstringpersonality.md)
  Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [static var integerPersonality: NSPointerFunctions.Options](./options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](./options/objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var objectPointerPersonality: NSPointerFunctions.Options](./options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](./options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](./options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](./sizefunction.md)).
- [var NSMapTableObjectPointerPersonality: NSPointerFunctions.Options](../nsmaptableobjectpointerpersonality.md)
  Equivalent to [`objectPointerPersonality`](./options/objectpointerpersonality.md).
### Copy Option
- [static var copyIn: NSPointerFunctions.Options](./options/copyin.md)
  Use the memory acquire function to allocate and copy items on input (see [`acquireFunction`](./acquirefunction.md)).
- [var NSMapTableCopyIn: NSPointerFunctions.Options](../nsmaptablecopyin.md)
  Equivalent to [`copyIn`](./options/copyin.md).
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options)*