# weakMemory

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```c
NSPointerFunctionsWeakMemory
```

## See Also

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](./machvirtualmemory.md)
  Use Mach memory.
- [static var mallocMemory: NSPointerFunctions.Options](./mallocmemory.md)
  Use `free()` on removal, `calloc()` on copy in.
- [static var opaqueMemory: NSPointerFunctions.Options](./opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](./strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [var NSMapTableStrongMemory: NSPointerFunctions.Options](../../nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](./strongmemory.md).
- [var NSMapTableWeakMemory: NSPointerFunctions.Options](../../nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](./weakmemory.md).
- [NSPointerFunctionsZeroingWeakMemory](../../nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md)
  Use weak read and write barriers; use garbage-collected memory on copyIn.
- [NSMapTableZeroingWeakMemory](../../nsmaptablezeroingweakmemory.md)
  Equivalent to [`NSPointerFunctionsZeroingWeakMemory`](../../nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/weakmemory)*