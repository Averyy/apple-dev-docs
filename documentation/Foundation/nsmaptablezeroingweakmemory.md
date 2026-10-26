# NSMapTableZeroingWeakMemory

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Equivalent to [`NSPointerFunctionsZeroingWeakMemory`](./nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

## Declaration

```c
static const NSPointerFunctionsOptions NSMapTableZeroingWeakMemory;
```

## See Also

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](./nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](./nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](./nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](./nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](./nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [NSPointerFunctionsZeroingWeakMemory](./nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md)
  Use weak read and write barriers; use garbage-collected memory on copyIn.
- [var NSMapTableStrongMemory: NSPointerFunctions.Options](./nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](./nspointerfunctions/options/strongmemory.md).
- [var NSMapTableWeakMemory: NSPointerFunctions.Options](./nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](./nspointerfunctions/options/weakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablezeroingweakmemory)*