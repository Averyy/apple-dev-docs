# weakMemory

**Framework**: Foundation  
**Kind**: property

Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var weakMemory: NSPointerFunctions.Options { get }
```

## See Also

- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var machVirtualMemory: NSPointerFunctions.Options](nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [let NSMapTableStrongMemory: NSPointerFunctions.Options](nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSMapTableWeakMemory: NSPointerFunctions.Options](nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](nspointerfunctions/options/weakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/weakmemory)*