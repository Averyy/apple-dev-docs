# NSPointerFunctionsZeroingWeakMemory

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

Use weak read and write barriers; use garbage-collected memory on copyIn.

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

## Declaration

```c
NSPointerFunctionsZeroingWeakMemory
```

## Discussion

If you do not use garbage collection, for object personalities, it will hold a non-retained object pointer.

## See Also

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](../nspointerfunctions/options/machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](../nspointerfunctions/options/mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](../nspointerfunctions/options/opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](../nspointerfunctions/options/strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](../nspointerfunctions/options/weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [var NSMapTableStrongMemory: NSPointerFunctions.Options](../nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](../nspointerfunctions/options/strongmemory.md).
- [var NSMapTableWeakMemory: NSPointerFunctions.Options](../nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](../nspointerfunctions/options/weakmemory.md).
- [NSMapTableZeroingWeakMemory](../nsmaptablezeroingweakmemory.md)
  Equivalent to [`NSPointerFunctionsZeroingWeakMemory`](./nspointerfunctionszeroingweakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory)*