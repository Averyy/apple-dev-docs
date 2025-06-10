# strongMemory

**Framework**: Foundation  
**Kind**: property

Use strong write-barriers to backing store; use garbage-collected memory on copy-in.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var strongMemory: NSPointerFunctions.Options { get }
```

#### Discussion

This is the default memory value.

As a special case, if you do not use garbage collection and specify this value in conjunction with [`objectPersonality`](nspointerfunctions/options/objectpersonality.md) or [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md) then the `NSPointerFunctions` object uses `retain` and `release`.

If you do not use garbage collection, and specify this value in conjunction with a valid non-object personality, it is the same as specifying [`mallocMemory`](nspointerfunctions/options/mallocmemory.md).

## See Also

- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var weakMemory: NSPointerFunctions.Options](nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var weakMemory: NSPointerFunctions.Options](nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [let NSMapTableStrongMemory: NSPointerFunctions.Options](nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSMapTableWeakMemory: NSPointerFunctions.Options](nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](nspointerfunctions/options/weakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/strongmemory)*