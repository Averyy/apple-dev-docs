# mallocMemory

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Use `free()` on removal, `calloc()` on copy in.

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
static var mallocMemory: NSPointerFunctions.Options { get }
```

```c
NSPointerFunctionsMallocMemory
```

## See Also

### Memory Options
- [static var machVirtualMemory: NSPointerFunctions.Options](./machvirtualmemory.md)
  Use Mach memory.
- [static var opaqueMemory: NSPointerFunctions.Options](./opaquememory.md)
  Take no action when pointers are deleted.
- [static var strongMemory: NSPointerFunctions.Options](./strongmemory.md)
  Use strong write-barriers to backing store; use garbage-collected memory on copy-in.
- [static var weakMemory: NSPointerFunctions.Options](./weakmemory.md)
  Uses weak read and write barriers appropriate for ARC or GC. Using NSPointerFunctionsWeakMemory object references will turn to `NULL` on last release.
- [var NSMapTableStrongMemory: NSPointerFunctions.Options](../../nsmaptablestrongmemory.md)
  Equivalent to [`strongMemory`](./strongmemory.md).
- [var NSMapTableWeakMemory: NSPointerFunctions.Options](../../nsmaptableweakmemory.md)
  Equivalent to [`weakMemory`](./weakmemory.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/mallocmemory)*