# NSPointerFunctions.Options

**Framework**: Foundation  
**Kind**: struct

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

#### Overview

When specifying a value, you can use only one of the options listed in Memory Options,  only one of the options listed in Personality Options, and any number of other options.

## Topics

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [let NSMapTableStrongMemory: NSPointerFunctions.Options](nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSMapTableWeakMemory: NSPointerFunctions.Options](nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](nspointerfunctions/options/weakmemory.md).
### Personality Options
- [static var cStringPersonality: NSPointerFunctions.Options](nspointerfunctions/options/cstringpersonality.md)
  Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [static var integerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var objectPointerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](nspointerfunctions/options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](nspointerfunctions/options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](nspointerfunctions/sizefunction.md)).
- [static var cStringPersonality: NSPointerFunctions.Options](nspointerfunctions/options/cstringpersonality.md)
  Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [static var integerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/integerpersonality.md)
  Use unshifted value as hash and equality.
- [static var objectPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpersonality.md)
  Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [static var objectPointerPersonality: NSPointerFunctions.Options](nspointerfunctions/options/objectpointerpersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [static var opaquePersonality: NSPointerFunctions.Options](nspointerfunctions/options/opaquepersonality.md)
  Use shifted pointer for the hash value and direct comparison to determine equality.
- [static var structPersonality: NSPointerFunctions.Options](nspointerfunctions/options/structpersonality.md)
  Use a memory hash and `memcmp` (using a size function that you must set—see [`sizeFunction`](nspointerfunctions/sizefunction.md)).
- [let NSMapTableObjectPointerPersonality: NSPointerFunctions.Options](nsmaptableobjectpointerpersonality.md)
  Equivalent to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).
### Copy Option
- [static var copyIn: NSPointerFunctions.Options](nspointerfunctions/options/copyin.md)
  Use the memory acquire function to allocate and copy items on input (see [`acquireFunction`](nspointerfunctions/acquirefunction.md)).
- [static var copyIn: NSPointerFunctions.Options](nspointerfunctions/options/copyin.md)
  Use the memory acquire function to allocate and copy items on input (see [`acquireFunction`](nspointerfunctions/acquirefunction.md)).
- [let NSMapTableCopyIn: NSPointerFunctions.Options](nsmaptablecopyin.md)
  Equivalent to [`copyIn`](nspointerfunctions/options/copyin.md).
### Initializers
- [init(rawValue: UInt)](nspointerfunctions/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options)*